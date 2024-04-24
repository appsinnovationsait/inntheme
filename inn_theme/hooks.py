app_name = "inn_theme"
app_title = "Inn Theme"
app_publisher = "innovation-sa"
app_description = "Custom theme changes"
app_email = "support@innovation-sa.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/inn_theme/css/inn_theme.css"
app_include_css = ["inn_theme.bundle.css"]
app_include_js = ["inn_theme_desk.bundle.js"]
# app_include_js = "/assets/inn_theme/js/inn_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/inn_theme/css/inn_theme.css"
# web_include_js = "/assets/inn_theme/js/inn_theme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "inn_theme/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "inn_theme.utils.jinja_methods",
# 	"filters": "inn_theme.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "inn_theme.install.before_install"
# after_install = "inn_theme.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "inn_theme.uninstall.before_uninstall"
# after_uninstall = "inn_theme.uninstall.after_uninstall"

after_migrate = [
    "inn_theme.workspace_icon_set.update_workspace_images",
]

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "inn_theme.utils.before_app_install"
# after_app_install = "inn_theme.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "inn_theme.utils.before_app_uninstall"
# after_app_uninstall = "inn_theme.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "inn_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"inn_theme.tasks.all"
# 	],
# 	"daily": [
# 		"inn_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"inn_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"inn_theme.tasks.weekly"
# 	],
# 	"monthly": [
# 		"inn_theme.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "inn_theme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "inn_theme.event.get_events"
# }
override_whitelisted_methods = {
    "frappe.desk.desktop.get_workspace_sidebar_items": "inn_theme.workspace_icon_set.get_workspace_sidebar_items",
    "frappe.core.doctype.user.user.switch_theme": "inn_theme.core.doctype.user.user.switch_theme",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "inn_theme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["inn_theme.utils.before_request"]
# after_request = ["inn_theme.utils.after_request"]

# Job Events
# ----------
# before_job = ["inn_theme.utils.before_job"]
# after_job = ["inn_theme.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"inn_theme.auth.validate"
# ]

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["dt", "=", "Workspace"], ["is_system_generated", "=", 0]],
    }
]