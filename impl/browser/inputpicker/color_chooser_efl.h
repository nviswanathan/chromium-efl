/*
    Copyright (C) 2014 Samsung Electronics

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

#ifndef ColorChooserEfl_h
#define ColorChooserEfl_h

#include "content/public/browser/color_chooser.h"
#include "third_party/skia/include/core/SkColor.h"

#include <Evas.h>

namespace content {

class ColorChooser;
class WebContents;
class WebContentsDelegateEfl;

class ColorChooserEfl : public ColorChooser {
 public:
  ColorChooserEfl(WebContents* web_contents);
  ~ColorChooserEfl();

  // ColorChooser implementation.
  virtual void SetSelectedColor(SkColor color);
  virtual void End();
  void SetWebContentsDelegateEfl(WebContents* web_contents);

 private:
  WebContentsDelegateEfl* web_contents_delegate_;
};

}

#endif // ColorChooserEfl_h