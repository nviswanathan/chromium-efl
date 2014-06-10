/*
   Copyright (C) 2013 Samsung Electronics

   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Library General Public
   License as published by the Free Software Foundation; either
   version 2 of the License, or (at your option) any later version.

   This library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Library General Public License for more details.

   You should have received a copy of the GNU Library General Public License
   along with this library; see the file COPYING.LIB.  If not, write to
   the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.
*/

#include "eweb_view.h"
#include "selection_controller_efl.h"
#include "selection_handle_efl.h"
#include "selection_box_efl.h"
#include "selection_magnifier_efl.h"

namespace content {

static bool IsRectEmpty(const gfx::Rect& rect) {
  if (rect.x() == 0 && rect.y() == 0 && rect.height() == 0 && rect.width() == 0) {
    LOG(INFO) << "SelectionControllerEfl:IsRectEmpty : true";
    return true;
  }
  return false;
}

SelectionControllerEfl::SelectionControllerEfl(EWebView* parent_view)
    :  parent_view_(parent_view),
       mouse_press_(false),
       long_mouse_press_(false),
       scrolling_(false),
       selection_data_(new SelectionBoxEfl(parent_view)),
       start_handle_(new SelectionHandleEfl(this, SelectionHandleEfl::HANDLE_TYPE_LEFT, parent_view->evas_object())),
       end_handle_(new SelectionHandleEfl(this, SelectionHandleEfl::HANDLE_TYPE_RIGHT, parent_view->evas_object())),
       input_handle_(new SelectionHandleEfl(this, SelectionHandleEfl::HANDLE_TYPE_INPUT, parent_view->evas_object())),
       magnifier_(new SelectionMagnifierEfl(this)) {
  evas_object_event_callback_add(parent_view_->evas_object(), EVAS_CALLBACK_MOVE, &EvasParentViewMoveCallback, this);
}

void SelectionControllerEfl::SetSelectionStatus(bool enable) {
  LOG(INFO) << "SelectionControllerEfl::SetSelectionStatus " << enable;
  selection_data_->SetStatus(enable);
}

bool SelectionControllerEfl::GetSelectionStatus() const {
  LOG(INFO) << "SelectionControllerEfl::GetSelectionStatus " << selection_data_->GetStatus();
  return selection_data_->GetStatus();
}

void SelectionControllerEfl::SetSelectionEditable(bool enable) {
  LOG(INFO) << "SelectionControllerEfl::SetSelectionEditable" << enable;
  selection_data_->SetEditable(enable);
}

bool SelectionControllerEfl::GetSelectionEditable() const {
  LOG(INFO) << "SelectionControllerEfl::GetSelectionEditable " << selection_data_->GetEditable();
  return selection_data_->GetEditable();
}

void SelectionControllerEfl::SetCaretSelectionStatus(const bool enable) {
  LOG(INFO) << "SelectionControllerEfl::SetCaretSelectionStatus : " << enable;
  selection_data_->SetCaretSelectionStatus(enable);
}

bool SelectionControllerEfl::GetCaretSelectionStatus() const {
  LOG(INFO) << "SelectionControllerEfl::GetCaretSelectionStatus : " << selection_data_->GetCaretSelectionStatus();
  return selection_data_->GetCaretSelectionStatus();
}

void SelectionControllerEfl::SetScrollStatus(const bool enable) {
  LOG(INFO) << __PRETTY_FUNCTION__ << " enable : " << enable;
  scrolling_ = enable;
  if (enable)
    Clear();
  else
    ShowHandleAndContextMenuIfRequired();
}

bool SelectionControllerEfl::GetScrollStatus() {
  LOG(INFO) << __PRETTY_FUNCTION__ << " " << scrolling_;
  return scrolling_;
}

void SelectionControllerEfl::UpdateSelectionData(const base::string16& text) {
  selection_data_->UpdateSelectStringData(text);
}

void SelectionControllerEfl::UpdateMagnifierScreen(Evas_Object* img) {
  magnifier_->UpdateScreen(img);
}

void SelectionControllerEfl::UpdateSelectionDataAndShow(const gfx::Rect& left_rect, const gfx::Rect& right_rect, bool is_anchor_first) {
  LOG(INFO) << __PRETTY_FUNCTION__;
  selection_data_->UpdateRectData(left_rect, right_rect, is_anchor_first);

  if (!IsSelectionValid(left_rect, right_rect)) {
    Clear();
    return;
  }

  // Do not show the context menu and handlers untill long mouse press is released
  if (long_mouse_press_)
    return;

  // Do not show the context menu and handlers while page is scrolling
  if (scrolling_)
    return;

  ShowHandleAndContextMenuIfRequired();
}

void SelectionControllerEfl::ShowHandleAndContextMenuIfRequired() {
  LOG(INFO) << __PRETTY_FUNCTION__;
  if (!selection_data_->GetStatus())
    return;

  Clear();

  // Is in edit field and no text is selected. show only single handle
  if (selection_data_->IsInEditField() && GetCaretSelectionStatus()) {
    gfx::Rect left = selection_data_->GetLeftRect();
    input_handle_->SetBasePosition(gfx::Point(left.x(), left.y()));
    input_handle_->SetCursorHandlerStatus(true);
    input_handle_->Move(gfx::Point(left.x(), left.y() + left.height()));
    input_handle_->Show();

    if (!mouse_press_)
      parent_view_->ShowContextMenu(*(selection_data_->GetContextMenuParams()), MENU_TYPE_SELECTION);

    return;
  }

  // FIXME : Check the text Direction later
  gfx::Rect left = selection_data_->GetLeftRect();
  // The base position of start_handle should be set to the middle of the left rectangle.
  // Otherwise the start_handle may be shifted up when the right_handle is moving
  start_handle_->SetBasePosition(gfx::Point(left.x(), left.y() + (left.height() / 2)));
  start_handle_->Move(gfx::Point(left.x(), left.y() + left.height()));
  start_handle_->Show();

  gfx::Rect right = selection_data_->GetRightRect();

  // The base position of end_handle should be set to the middle of the right rectangle.
  // Otherwise the end_handle may be shifted up when the left_handle is moving
  end_handle_->SetBasePosition(gfx::Point(right.x(), right.y() + (right.height() / 2)));
  end_handle_->Move(gfx::Point(right.x() + right.width(), right.y() + right.height()));
  end_handle_->Show();

  // Do not show the context menu during selection extend
  if (!mouse_press_)
    parent_view_->ShowContextMenu(*(selection_data_->GetContextMenuParams()), MENU_TYPE_SELECTION);
  parent_view_->QuerySelectionStyle();
}

void SelectionControllerEfl::HideHandle() {
  SetCaretSelectionStatus(false);
  Clear();
}

void SelectionControllerEfl::HideHandleAndContextMenu() {
  parent_view_->CancelContextMenu(0);
  HideHandle();
}

void SelectionControllerEfl::Clear() {
  start_handle_->Hide();
  end_handle_->Hide();
  input_handle_->Hide();
}

void SelectionControllerEfl::OnMouseDown(const gfx::Point& touch_point) {
  // Hide context menu on mouse down
  parent_view_->CancelContextMenu(0);
  mouse_press_ = true;
  magnifier_->UpdateLocation(touch_point);
  magnifier_->Move(touch_point);
  ShowHandleAndContextMenuIfRequired();
}

void SelectionControllerEfl::OnMouseMove(const gfx::Point& touch_point, bool on_curson_handle) {
  // FIXME : Check the text Direction later
  magnifier_->UpdateLocation(touch_point);
  magnifier_->Move(touch_point);
  if (!on_curson_handle)
    parent_view_->SelectRange(start_handle_->GetBasePosition(), end_handle_->GetBasePosition());
  else
    parent_view_->MoveCaret(input_handle_->GetBasePosition());
}

void SelectionControllerEfl::OnMouseUp(const gfx::Point& touch_point) {
  selection_data_->UpdateHandleData();
  mouse_press_ = false;
  magnifier_->Hide();
  parent_view_->ShowContextMenu(*(selection_data_->GetContextMenuParams()), MENU_TYPE_SELECTION);
}

void SelectionControllerEfl::GetSelectionBounds(gfx::Rect* left, gfx::Rect* right) {
  if (left)
    *left = selection_data_->GetLeftRect();
  if (right)
    *right = selection_data_->GetRightRect();
}

void SelectionControllerEfl::HandleLongPressEvent(const gfx::Point& touch_point) {
  long_mouse_press_ = true;
  magnifier_->HandleLongPress(touch_point);
}

void SelectionControllerEfl::HandleLongPressMoveEvent(const gfx::Point& touch_point) {
  parent_view_->SelectClosestWord(touch_point);

  if (selection_data_->GetCaretSelectionStatus()) {
    parent_view_->MoveCaret(touch_point);
    SetSelectionStatus(true);
    ShowHandleAndContextMenuIfRequired();
  } else{
    parent_view_->SelectClosestWord(touch_point);
  }
}

void SelectionControllerEfl::HandleLongPressEndEvent() {
  long_mouse_press_ = false;
  if (selection_data_->GetCaretSelectionStatus()) {
    SetSelectionStatus(true);
    SetSelectionEditable(true);
  }
  ShowHandleAndContextMenuIfRequired();
}

bool SelectionControllerEfl::IsSelectionValid(const gfx::Rect& left_rect, const gfx::Rect& right_rect) {
  LOG(INFO) << __PRETTY_FUNCTION__ << " l_x = " << left_rect.x() << " l_y = " << left_rect.y() << " r_x = " << right_rect.x() << " r_y = " << right_rect.y();
  // For all normal cases the widht will be 0 and we want to check empty which Implies
  // x, y, h w all to be 0
  if ((IsRectEmpty(left_rect) || IsRectEmpty(right_rect))) {
    SetSelectionStatus(false);
    return false;
  }

  // The most of sites return width of each rects as 0 when text is selected.
  // However, some websites that have viewport attributes on meta tag v
  // return width 0 right after they are loaded, even though text is not selected.
  // Thus the width is not sufficient for checking selection condition.
  // Further invesitigation showed left_rect and right_rect always have the same x,y values
  // for such cases. So, the equality for x and y rather than width should be tested.
  if (left_rect.x()==right_rect.x() && left_rect.y()==right_rect.y() &&
      !selection_data_->IsInEditField() && !mouse_press_) {
    SetSelectionStatus(false);
    return false;
  }

  LOG(INFO) << "SelectionControllerEfl::IsSelectionValid true";
  if (!GetSelectionStatus())
    SetSelectionStatus(true);

  if (left_rect.x() != right_rect.x() || left_rect.y() != right_rect.y() &&
      selection_data_->IsInEditField() && GetCaretSelectionStatus()) {
    if (!long_mouse_press_)
      SetCaretSelectionStatus(false);
  }

  LOG(INFO) << "SelectionControllerEfl::IsSelectionValid true";
  return true;
}

void SelectionControllerEfl::ClearSelection() {
  LOG(INFO) << __PRETTY_FUNCTION__;
  Clear();
  selection_data_->SetStatus(false);
  SetSelectionEditable(false);
  SetCaretSelectionStatus(false);
}

void SelectionControllerEfl::OnParentParentViewMove() {
  LOG(INFO) << __PRETTY_FUNCTION__;
  parent_view_->CancelContextMenu(0);
  start_handle_->Move(start_handle_->GetBasePosition());
  end_handle_->Move(end_handle_->GetBasePosition());
}

gfx::Rect SelectionControllerEfl::GetLeftRect() {
  return selection_data_->GetLeftRect();
}

gfx::Rect SelectionControllerEfl::GetRightRect() {
  return selection_data_->GetRightRect();
}

}
