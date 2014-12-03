{
  'targets': [{
    'target_name': 'ewk_unittests',
    'type': '<(gtest_target_type)',
    'dependencies': [
      '<(chrome_src_dir)/testing/gtest.gyp:gtest',
      'chromium-ewk',
    ],
    'include_dirs': [
      '../efl_integration/public',
    ],
    'sources': [
        'execute_utc_blink.cpp',
        'utc_blink_cb_contextmenu_allowed.cpp',
        'utc_blink_cb_contextmenu_willshow.cpp',
        'utc_blink_cb_editorclient_candidate_closed.cpp',
        'utc_blink_cb_editorclient_candidate_opened.cpp',
        'utc_blink_cb_editorclient_ime_closed.cpp',
        'utc_blink_cb_editorclient_ime_opened.cpp',
        'utc_blink_cb_form_submit.cpp',
        'utc_blink_cb_fullscreen_enterfullscreen.cpp',
        'utc_blink_cb_fullscreen_exitfullscreen.cpp',
        'utc_blink_cb_geolocation_valid.cpp',
        'utc_blink_cb_icon_received.cpp',
        'utc_blink_cb_inputmethod_changed.cpp',
        'utc_blink_cb_load_finished.cpp',
        'utc_blink_cb_load_progress.cpp',
        'utc_blink_cb_load_progress_finished.cpp',
        'utc_blink_cb_load_progress_started.cpp',
        'utc_blink_cb_load_started.cpp',
        'utc_blink_cb_magnifier_hide.cpp',
        'utc_blink_cb_magnifier_show.cpp',
        'utc_blink_cb_popup_blocked.cpp',
        'utc_blink_cb_protocolhandler_isregistered.cpp',
        'utc_blink_cb_protocolhandler_registration_requested.cpp',
        'utc_blink_cb_protocolhandler_unregistration_requested.cpp',
        'utc_blink_cb_redo_size.cpp',
        'utc_blink_cb_textselection_mode.cpp',
        'utc_blink_cb_title_changed.cpp',
        'utc_blink_cb_undo_size.cpp',
        'utc_blink_cb_unfocus_direction.cpp',
        'utc_blink_cb_uri_changed.cpp',
        'utc_blink_cb_url_changed.cpp',
        'utc_blink_ewk_auth_challenge_credential_cancel_func.cpp',
        'utc_blink_ewk_auth_challenge_credential_use_func.cpp',
        'utc_blink_ewk_auth_challenge_realm_get_func.cpp',
        'utc_blink_ewk_auth_challenge_suspend_func.cpp',
        'utc_blink_ewk_autofill_profile_data_get_func.cpp',
        'utc_blink_ewk_autofill_profile_data_set_func.cpp',
        'utc_blink_ewk_autofill_profile_delete_func.cpp',
        'utc_blink_ewk_autofill_profile_new_func.cpp',
        'utc_blink_ewk_back_forward_list_count_func.cpp',
        'utc_blink_ewk_back_forward_list_current_item_get_func.cpp',
        'utc_blink_ewk_back_forward_list_item_at_index_get_func.cpp',
        'utc_blink_ewk_back_forward_list_item_original_url_get_func.cpp',
        'utc_blink_ewk_back_forward_list_item_ref_func.cpp',
        'utc_blink_ewk_back_forward_list_item_title_get_func.cpp',
        'utc_blink_ewk_back_forward_list_item_unref_func.cpp',
        'utc_blink_ewk_back_forward_list_item_url_get_func.cpp',
        'utc_blink_ewk_back_forward_list_n_back_items_copy_func.cpp',
        'utc_blink_ewk_back_forward_list_n_forward_items_copy_func.cpp',
        'utc_blink_ewk_back_forward_list_next_item_get_func.cpp',
        'utc_blink_ewk_back_forward_list_previous_item_get_func.cpp',
        'utc_blink_ewk_base.cpp',
        'utc_blink_ewk_base.h',
        'utc_blink_ewk_certificate_policy_decision_allowed_set_func.cpp',
        'utc_blink_ewk_certificate_policy_decision_certificate_pem_get_func.cpp',
        'utc_blink_ewk_certificate_policy_decision_suspend_func.cpp',
        'utc_blink_ewk_certificate_policy_decision_url_get_func.cpp',
        'utc_blink_ewk_console_message_level_get_func.cpp',
        'utc_blink_ewk_console_message_line_get_func.cpp',
        'utc_blink_ewk_console_message_source_get_func.cpp',
        'utc_blink_ewk_console_message_text_get_func.cpp',
        'utc_blink_ewk_context_additional_plugin_path_set_func.cpp',
        'utc_blink_ewk_context_application_cache_delete_all_func.cpp',
        'utc_blink_ewk_context_application_cache_delete_func.cpp',
        'utc_blink_ewk_context_application_cache_origins_get_func.cpp',
        'utc_blink_ewk_context_cache_clear_func.cpp',
        'utc_blink_ewk_context_cache_disabled_set_func.cpp',
        'utc_blink_ewk_context_cache_model_get_func.cpp',
        'utc_blink_ewk_context_cache_model_set_func.cpp',
        'utc_blink_ewk_context_certificate_file_get_func.cpp',
        'utc_blink_ewk_context_certificate_file_set_func.cpp',
        'utc_blink_ewk_context_cookie_manager_get_func.cpp',
        'utc_blink_ewk_context_default_get_func.cpp',
        'utc_blink_ewk_context_delete_func.cpp',
        'utc_blink_ewk_context_did_start_download_callback_set_func.cpp',
        'utc_blink_ewk_context_form_autofill_profile_add_func.cpp',
        'utc_blink_ewk_context_form_autofill_profile_get_all_func.cpp',
        'utc_blink_ewk_context_form_autofill_profile_get_func.cpp',
        'utc_blink_ewk_context_form_autofill_profile_remove_func.cpp',
        'utc_blink_ewk_context_form_autofill_profile_set_func.cpp',
        'utc_blink_ewk_context_form_autofill_profile_utils.cpp',
        'utc_blink_ewk_context_form_autofill_profile_utils.h',
        'utc_blink_ewk_context_form_candidate_data_delete_all_func.cpp',
        'utc_blink_ewk_context_form_password_data_delete_all_func.cpp',
        'utc_blink_ewk_context_icon_database_icon_object_add_func.cpp',
        'utc_blink_ewk_context_icon_database_path_set_func.cpp',
        'utc_blink_ewk_context_local_file_system_all_delete_func.cpp',
        'utc_blink_ewk_context_local_file_system_delete_func.cpp',
        'utc_blink_ewk_context_memory_sampler_start_func.cpp',
        'utc_blink_ewk_context_memory_sampler_stop_func.cpp',
        'utc_blink_ewk_context_menu.h',
        'utc_blink_ewk_context_menu_item_append_as_action_func.cpp',
        'utc_blink_ewk_context_menu_item_append_func.cpp',
        'utc_blink_ewk_context_menu_item_count_func.cpp',
        'utc_blink_ewk_context_menu_item_image_url_get_func.cpp',
        'utc_blink_ewk_context_menu_item_link_url_get_func.cpp',
        'utc_blink_ewk_context_menu_item_remove_func.cpp',
        'utc_blink_ewk_context_menu_item_tag_get_func.cpp',
        'utc_blink_ewk_context_menu_nth_item_get_func.cpp',
        'utc_blink_ewk_context_new_func.cpp',
        'utc_blink_ewk_context_notify_low_memory_func.cpp',
        'utc_blink_ewk_context_pixmap_set_func.cpp',
        'utc_blink_ewk_context_preferred_languages_set_func.cpp',
        'utc_blink_ewk_context_proxy_uri_get_func.cpp',
        'utc_blink_ewk_context_proxy_uri_set_func.cpp',
        'utc_blink_ewk_context_vibration_client_callbacks_set_func.cpp',
        'utc_blink_ewk_context_web_database_delete_all_func.cpp',
        'utc_blink_ewk_context_web_database_delete_func.cpp',
        'utc_blink_ewk_context_web_database_origins_get_func.cpp',
        'utc_blink_ewk_context_web_indexed_database_delete_all_func.cpp',
        'utc_blink_ewk_context_web_storage_delete_all_func.cpp',
        'utc_blink_ewk_context_web_storage_origin_delete_func.cpp',
        'utc_blink_ewk_context_web_storage_origins_get_func.cpp',
        'utc_blink_ewk_cookie_manager_accept_policy_async_get_func.cpp',
        'utc_blink_ewk_cookie_manager_accept_policy_set_func.cpp',
        'utc_blink_ewk_cookie_manager_cookies_clear_func.cpp',
        'utc_blink_ewk_custom_handlers_data_base_url_get_func.cpp',
        'utc_blink_ewk_custom_handlers_data_result_set_func.cpp',
        'utc_blink_ewk_custom_handlers_data_target_get_func.cpp',
        'utc_blink_ewk_custom_handlers_data_title_get_func.cpp',
        'utc_blink_ewk_custom_handlers_data_url_get_func.cpp',
        'utc_blink_ewk_error_code_get_func.cpp',
        'utc_blink_ewk_error_description_get_func.cpp',
        'utc_blink_ewk_error_type_get_func.cpp',
        'utc_blink_ewk_error_url_get_func.cpp',
        'utc_blink_ewk_frame_is_main_frame_func.cpp',
        'utc_blink_ewk_geolocation_permission_request_origin_get_func.cpp',
        'utc_blink_ewk_geolocation_permission_request_set_func.cpp',
        'utc_blink_ewk_geolocation_permission_request_suspend_func.cpp',
        'utc_blink_ewk_history_back_list_length_get_func.cpp',
        'utc_blink_ewk_history_forward_list_length_get.cpp',
        'utc_blink_ewk_history_free_func.cpp',
        'utc_blink_ewk_history_item_title_get_func.cpp',
        'utc_blink_ewk_history_item_uri_get_func.cpp',
        'utc_blink_ewk_history_nth_item_get.cpp',
        'utc_blink_ewk_hit_test_attribute_hash_get_func.cpp',
        'utc_blink_ewk_hit_test_free_func.cpp',
        'utc_blink_ewk_hit_test_image_buffer_get_func.cpp',
        'utc_blink_ewk_hit_test_image_buffer_length_get_func.cpp',
        'utc_blink_ewk_hit_test_image_file_name_extension_get_func.cpp',
        'utc_blink_ewk_hit_test_image_uri_get_func.cpp',
        'utc_blink_ewk_hit_test_link_label_get_func.cpp',
        'utc_blink_ewk_hit_test_link_title_get_func.cpp',
        'utc_blink_ewk_hit_test_link_uri_get_func.cpp',
        'utc_blink_ewk_hit_test_media_uri_get_func.cpp',
        'utc_blink_ewk_hit_test_node_value_get_func.cpp',
        'utc_blink_ewk_hit_test_result_context_get_func.cpp',
        'utc_blink_ewk_hit_test_tag_name_get_func.cpp',
        'utc_blink_ewk_home_directory_get_func.cpp',
        'utc_blink_ewk_home_directory_set_func.cpp',
        'utc_blink_ewk_notification_body_get_func.cpp',
        'utc_blink_ewk_notification_clicked_func.cpp',
        'utc_blink_ewk_notification_icon_url_get_func.cpp',
        'utc_blink_ewk_notification_id_get_func.cpp',
        'utc_blink_ewk_notification_permission_request_origin_get_func.cpp',
        'utc_blink_ewk_notification_permission_request_set_func.cpp',
        'utc_blink_ewk_notification_permission_request_suspend_func.cpp',
        'utc_blink_ewk_notification_security_origin_get_func.cpp',
        'utc_blink_ewk_notification_showed_func.cpp',
        'utc_blink_ewk_notification_title_get_func.cpp',
        'utc_blink_ewk_policy_decision_cookie_get_func.cpp',
        'utc_blink_ewk_policy_decision_frame_get_func.cpp',
        'utc_blink_ewk_policy_decision_host_get_func.cpp',
        'utc_blink_ewk_policy_decision_http_method_get_func.cpp',
        'utc_blink_ewk_policy_decision_ignore_func.cpp',
        'utc_blink_ewk_policy_decision_navigation_type_get_func.cpp',
        'utc_blink_ewk_policy_decision_password_get_func.cpp',
        'utc_blink_ewk_policy_decision_response_headers_get_func.cpp',
        'utc_blink_ewk_policy_decision_response_mime_get_func.cpp',
        'utc_blink_ewk_policy_decision_response_status_code_get_func.cpp',
        'utc_blink_ewk_policy_decision_scheme_get_func.cpp',
        'utc_blink_ewk_policy_decision_suspend_func.cpp',
        'utc_blink_ewk_policy_decision_type_get_func.cpp',
        'utc_blink_ewk_policy_decision_url_get_func.cpp',
        'utc_blink_ewk_policy_decision_use_func.cpp',
        'utc_blink_ewk_policy_decision_userid_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_is_persistent_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_origin_host_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_origin_port_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_origin_protocol_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_quota_get_func.cpp',
        'utc_blink_ewk_security_origin_host_get_func.cpp',
        'utc_blink_ewk_security_origin_port_get_func.cpp',
        'utc_blink_ewk_security_origin_protocol_get_func.cpp',
        'utc_blink_ewk_settings_autofill_password_form_enabled_get_func.cpp',
        'utc_blink_ewk_settings_autofill_password_form_enabled_set_func.cpp',
        'utc_blink_ewk_settings_auto_fitting_get_func.cpp',
        'utc_blink_ewk_settings_auto_fitting_set_func.cpp',
        'utc_blink_ewk_settings_clear_text_selection_automatically_set_func.cpp',
        'utc_blink_ewk_settings_current_legacy_font_size_mode_set_func.cpp',
        'utc_blink_ewk_settings_default_encoding_set_func.cpp',
        'utc_blink_ewk_settings_default_keypad_enabled_set_func.cpp',
        'utc_blink_ewk_settings_detect_contents_automatically_set_func.cpp',
        'utc_blink_ewk_settings_edge_effect_enabled_set_func.cpp',
        'utc_blink_ewk_settings_editable_link_behavior_set_func.cpp',
        'utc_blink_ewk_settings_extra_feature_set_func.cpp',
        'utc_blink_ewk_settings_font_default_size_get_func.cpp',
        'utc_blink_ewk_settings_font_default_size_set_func.cpp',
        'utc_blink_ewk_settings_force_zoom_set_func.cpp',
        'utc_blink_ewk_settings_form_candidate_data_enabled_set_func.cpp',
        'utc_blink_ewk_settings_form_profile_data_enabled_get_func.cpp',
        'utc_blink_ewk_settings_form_profile_data_enabled_set_func.cpp',
        'utc_blink_ewk_settings_initial_list_style_position_get_func.cpp',
        'utc_blink_ewk_settings_initial_list_style_position_set_func.cpp',
        'utc_blink_ewk_settings_is_encoding_valid_func.cpp',
        'utc_blink_ewk_settings_javascript_enabled_get_func.cpp',
        'utc_blink_ewk_settings_javascript_enabled_set_func.cpp',
        'utc_blink_ewk_settings_link_effect_enabled_set_func.cpp',
        'utc_blink_ewk_settings_link_magnifier_enabled_get_func.cpp',
        'utc_blink_ewk_settings_link_magnifier_enabled_set_func.cpp',
        'utc_blink_ewk_settings_load_remote_images_set_func.cpp',
        'utc_blink_ewk_settings_loads_images_automatically_set_func.cpp',
        'utc_blink_ewk_settings_paste_image_uri_mode_set_func.cpp',
        'utc_blink_ewk_settings_plugins_enabled_set_func.cpp',
        'utc_blink_ewk_settings_scripts_can_open_windows_get_func.cpp',
        'utc_blink_ewk_settings_scripts_can_open_windows_set_func.cpp',
        'utc_blink_ewk_settings_scripts_window_open_get_func.cpp',
        'utc_blink_ewk_settings_scripts_window_open_set_func.cpp',
        'utc_blink_ewk_settings_select_word_automatically_set_func.cpp',
        'utc_blink_ewk_settings_spdy_enabled_set_func.cpp',
        'utc_blink_ewk_settings_text_autosizing_enabled_set_func.cpp',
        'utc_blink_ewk_settings_text_autosizing_font_scale_factor_set_func.cpp',
        'utc_blink_ewk_settings_text_selection_enabled_set_func.cpp',
        'utc_blink_ewk_settings_text_style_state_enabled_set_func.cpp',
        'utc_blink_ewk_settings_text_zoom_enabled_set_func.cpp',
        'utc_blink_ewk_settings_uses_encoding_detector_set_func.cpp',
        'utc_blink_ewk_settings_uses_keypad_without_user_action_set_func.cpp',
        'utc_blink_ewk_text_style_align_center_get_func.cpp',
        'utc_blink_ewk_text_style_align_full_get_func.cpp',
        'utc_blink_ewk_text_style_align_left_get_func.cpp',
        'utc_blink_ewk_text_style_align_right_get_func.cpp',
        'utc_blink_ewk_text_style_bg_color_get_func.cpp',
        'utc_blink_ewk_text_style_bold_get_func.cpp',
        'utc_blink_ewk_text_style_color_get_func.cpp',
        'utc_blink_ewk_text_style_font_size_get_func.cpp',
        'utc_blink_ewk_text_style_has_composition_get_func.cpp',
        'utc_blink_ewk_text_style_italic_get_func.cpp',
        'utc_blink_ewk_text_style_ordered_list_get_func.cpp',
        'utc_blink_ewk_text_style_position_get_func.cpp',
        'utc_blink_ewk_text_style_underline_get_func.cpp',
        'utc_blink_ewk_text_style_unordered_list_get_func.cpp',
        'utc_blink_ewk_user_media_permission_request_set_func.cpp',
        'utc_blink_ewk_user_media_permission_request_suspend_func.cpp',
        'utc_blink_ewk_view_add_func.cpp',
        'utc_blink_ewk_view_add_in_incognito_mode_func.cpp',
        'utc_blink_ewk_view_add_with_context_func.cpp',
        'utc_blink_ewk_view_add_with_session_data_func.cpp',
        'utc_blink_ewk_view_application_name_for_user_agent_get_func.cpp',
        'utc_blink_ewk_view_application_name_for_user_agent_set_func.cpp',
        'utc_blink_ewk_view_back_forward_list_clear_func.cpp',
        'utc_blink_ewk_view_back_forward_list_get_func.cpp',
        'utc_blink_ewk_view_back_func.cpp',
        'utc_blink_ewk_view_back_possible_func.cpp',
        'utc_blink_ewk_view_browser_font_set_func.cpp',
        'utc_blink_ewk_view_command_execute_func.cpp',
        'utc_blink_ewk_view_content_security_policy_set_func.cpp',
        'utc_blink_ewk_view_contents_pdf_get_func.cpp',
        'utc_blink_ewk_view_contents_set_func.cpp',
        'utc_blink_ewk_view_contents_size_get_func.cpp',
        'utc_blink_ewk_view_context_get_func.cpp',
        'utc_blink_ewk_view_custom_header_add_func.cpp',
        'utc_blink_ewk_view_custom_header_remove_func.cpp',
        'utc_blink_ewk_view_draws_transparent_background_set_func.cpp',
        'utc_blink_ewk_view_encoding_custom_set_func.cpp',
        'utc_blink_ewk_view_forward_func.cpp',
        'utc_blink_ewk_view_forward_possible_func.cpp',
        'utc_blink_ewk_view_fullscreen_exit_func.cpp',
        'utc_blink_ewk_view_geolocation_permission_callback_set_func.cpp',
        'utc_blink_ewk_view_get_cookies_for_url_func.cpp',
        'utc_blink_ewk_view_history_get_func.cpp',
        'utc_blink_ewk_view_hit_test_new_func.cpp',
        'utc_blink_ewk_view_hit_test_request_func.cpp',
        'utc_blink_ewk_view_html_contents_set_func.cpp',
        'utc_blink_ewk_view_html_string_load_func.cpp',
        'utc_blink_ewk_view_inspector_server_stop_func.cpp',
        'utc_blink_ewk_view_javascript_confirm_reply_func.cpp',
        'utc_blink_ewk_view_load_progress_get_func.cpp',
        'utc_blink_ewk_view_mhtml_data_get_func.cpp',
        'utc_blink_ewk_view_notification_closed_func.cpp',
        'utc_blink_ewk_view_orientation_lock_callback_set_func.cpp',
        'utc_blink_ewk_view_orientation_send_func.cpp',
        'utc_blink_ewk_view_page_visibility_state_set_func.cpp',
        'utc_blink_ewk_view_plain_text_get_func.cpp',
        'utc_blink_ewk_view_quota_permission_request_callback_set_func.cpp',
        'utc_blink_ewk_view_quota_permission_request_cancel_func.cpp',
        'utc_blink_ewk_view_quota_permission_request_reply_func.cpp',
        'utc_blink_ewk_view_reload_func.cpp',
        'utc_blink_ewk_view_resume_func.cpp',
        'utc_blink_ewk_view_scale_get_func.cpp',
        'utc_blink_ewk_view_scale_range_get_func.cpp',
        'utc_blink_ewk_view_scale_set_func.cpp',
        'utc_blink_ewk_view_screenshot_contents_get_func.cpp',
        'utc_blink_ewk_view_script_execute_func.cpp',
        'utc_blink_ewk_view_scroll_by_func.cpp',
        'utc_blink_ewk_view_scroll_pos_get_func.cpp',
        'utc_blink_ewk_view_scroll_set_func.cpp',
        'utc_blink_ewk_view_scroll_size_get_func.cpp',
        'utc_blink_ewk_view_session_data_get_func.cpp',
        'utc_blink_ewk_view_settings_get_func.cpp',
        'utc_blink_ewk_view_stop_func.cpp',
        'utc_blink_ewk_view_suspend_func.cpp',
        'utc_blink_ewk_view_text_find_func.cpp',
        'utc_blink_ewk_view_text_find_highlight_clear_func.cpp',
        'utc_blink_ewk_view_text_selection_clear_func.cpp',
        'utc_blink_ewk_view_text_selection_text_get_func.cpp',
        'utc_blink_ewk_view_text_zoom_get_func.cpp',
        'utc_blink_ewk_view_text_zoom_set_func.cpp',
        'utc_blink_ewk_view_title_get_func.cpp',
        'utc_blink_ewk_view_touch_events_enabled_set_func.cpp',
        'utc_blink_ewk_view_url_get_func.cpp',
        'utc_blink_ewk_view_url_request_set_func.cpp',
        'utc_blink_ewk_view_url_set_func.cpp',
        'utc_blink_ewk_view_user_agent_get_func.cpp',
        'utc_blink_ewk_view_user_agent_set_func.cpp',
        'utc_blink_ewk_view_use_settings_font_func.cpp',
        'utc_blink_ewk_view_visibility_set_func.cpp',
        'utc_blink_ewk_view_web_application_capable_get_func.cpp',
        'utc_blink_ewk_view_web_application_icon_url_get_func.cpp',
        'utc_blink_ewk_view_web_application_icon_urls_get_func.cpp',
        'utc_blink_ewk_web_application_icon_data_url_get_func.cpp',
    ],

    'cflags': [
      '<!@(pkg-config --cflags glib-2.0)',
    ],
    'link_settings': {
      'ldflags': [
        '<!@(pkg-config --libs-only-L --libs-only-other glib-2.0)',
      ],
      'libraries': [
        '<!@(pkg-config --libs-only-l glib-2.0)',
      ],
    },

    'conditions': [
     ['building_for_tizen==1', {
      'cflags': [
        '<!@(pkg-config --cflags scim)',
        '<!@(pkg-config --cflags x11)',
      ],
      'link_settings': {
        'ldflags': [
          '<!@(pkg-config --libs-only-L --libs-only-other scim)',
          '<!@(pkg-config --libs-only-L --libs-only-other x11)',
        ],
        'libraries': [
          '<!@(pkg-config --libs-only-l scim)',
          '<!@(pkg-config --libs-only-l x11)',
        ],
      },
    }],
    ['ewk_bringup==1', {
      'defines': [ 'EWK_BRINGUP=1' ],
      'sources!': [
        #XXX: enable *local_file_system* once we find a way to set --allow-file-access-from-files flag at runtime
        'utc_blink_ewk_context_local_file_system_all_delete_func.cpp',
        'utc_blink_ewk_context_local_file_system_delete_func.cpp',
        'utc_blink_ewk_history_back_list_length_get_func.cpp',
        'utc_blink_ewk_history_forward_list_length_get.cpp',
        'utc_blink_ewk_history_free_func.cpp',
        'utc_blink_ewk_history_item_title_get_func.cpp',
        'utc_blink_ewk_history_item_uri_get_func.cpp',
        'utc_blink_ewk_history_nth_item_get.cpp',
        'utc_blink_ewk_quota_permission_request_is_persistent_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_origin_host_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_origin_port_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_origin_protocol_get_func.cpp',
        'utc_blink_ewk_quota_permission_request_quota_get_func.cpp',
        'utc_blink_ewk_view_history_get_func.cpp',
        'utc_blink_ewk_view_quota_permission_request_callback_set_func.cpp',
        'utc_blink_ewk_view_quota_permission_request_cancel_func.cpp',
        'utc_blink_ewk_view_quota_permission_request_reply_func.cpp',
      ],
    }]
   ],

  }]
}
