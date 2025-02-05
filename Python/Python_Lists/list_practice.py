full_columns = [
                "site_name", "group_name", "username", "current_status", "full_name", "supervisor_name", "campaign",
                "app_idle_time", "dialer_idle_time", "pause_progressive_time", "progressive_time", "preview_time",
                "predictive_wait_time", "inbound_wait_time", "blended_wait_time", "ring_duration", "ring_duration_avg",
                "hold_time", "media_time", "predictive_wait_time_avg", "talk", "talk_avg", "bill_sec", "bill_sec_avg",
                "call_duration", "wrapup_time", "wrapup_time_average", "break_time", "break_time_avg", "app_login_time",
                "dialer_login_time", "total_login_time", "first_login_time", "last_logout_time", "total_calls",
                "total_unique_connected_calls", "date"
            ]
required_columns = [
                    "site_name", "group_name", "username", "current_status", "full_name", "campaign",
                    "app_idle_time", "dialer_idle_time", "predictive_wait_time", "ring_duration", 
                    "ring_duration_avg", "hold_time", "predictive_wait_time_avg", "talk", "bill_sec", 
                    "call_duration", "feedback_time", "break_time", "app_login_time", "dialer_login_time", 
                    "total_login_time", "first_login_time", "last_logout_time", "total_calls", 
                    "total_unique_connected_calls", "date"
                ]
op = [col for col in full_columns if col in required_columns]

print(op)