frappe.views.Workspace = class Custom_Workspace extends frappe.views.Workspace {

    _sidebar_item_container(item) {
        return $(`
			<div
				class="test sidebar-item-container ${item.is_editable ? "is-draggable" : ""}"
				item-parent="${item.parent_page}"
				item-name="${item.title}"
				item-public="${item.public || 0}"
				item-is-hidden="${item.is_hidden || 0}"
			>
				<div class="desk-sidebar-item standard-sidebar-item ${item.selected ? "selected" : ""}">
					<a
						href="/app/${item.public
                ? frappe.router.slug(item.title)
                : "private/" + frappe.router.slug(item.title)
            }"
						class="item-anchor ${item.is_editable ? "" : "block-click"}" title="${__(item.title)}"
					>
                    
						<span class="sidebar-item-icon" item-icon=${item.icon || "folder-normal"}>
                        ${item.custom_svg ? '<img class="icon-md mr-2" src=' + item.custom_svg + ' />' : frappe.utils.icon(item.icon || "folder-normal", "md")}
                        
                        
        </span>
						<span class="sidebar-item-label">${__(item.title)}<span>
					</a>
					<div class="sidebar-item-control"></div>
				</div>
				<div class="sidebar-child-item nested-container"></div>
			</div>
		`);
    }
}



frappe.ui.ThemeSwitcher = class Custom_ThemeSwitcher extends frappe.ui.ThemeSwitcher {
    fetch_themes() {
        return new Promise((resolve) => {
            this.themes = [
                {
                    name: "InnTheme",
                    label: __("Inn Cyan"),
                    info: __("Inn Cyan"),
                },
                {
                    name: "InnThemeBlue",
                    label: __("Inn Blue"),
                    info: __("Inn Blue"),
                },
                {
                    name: "InnThemePeach",
                    label: __("Inn Peach"),
                    info: __("Inn Peach"),
                },
                {
                    name: "light",
                    label: __("Frappe Light"),
                    info: __("Light Theme"),
                },
                {
                    name: "dark",
                    label: __("Timeless Night"),
                    info: __("Dark Theme"),
                },
                {
                    name: "automatic",
                    label: __("Automatic"),
                    info: __("Uses system's theme to switch between light and dark mode"),
                },
            ];

            resolve(this.themes);
        });
    }
}

