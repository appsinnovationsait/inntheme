(()=>{frappe.views.Workspace=class extends frappe.views.Workspace{_sidebar_item_container(e){return $(`
			<div
				class="test sidebar-item-container ${e.is_editable?"is-draggable":""}"
				item-parent="${e.parent_page}"
				item-name="${e.title}"
				item-public="${e.public||0}"
				item-is-hidden="${e.is_hidden||0}"
			>
				<div class="desk-sidebar-item standard-sidebar-item ${e.selected?"selected":""}">
					<a
						href="/app/${e.public?frappe.router.slug(e.title):"private/"+frappe.router.slug(e.title)}"
						class="item-anchor ${e.is_editable?"":"block-click"}" title="${__(e.title)}"
					>
                    
						<span class="sidebar-item-icon" item-icon=${e.icon||"folder-normal"}>
                        ${e.custom_svg?'<img class="icon-md mr-2" src='+e.custom_svg+" />":frappe.utils.icon(e.icon||"folder-normal","md")}
                        
                        
        </span>
						<span class="sidebar-item-label">${__(e.title)}<span>
					</a>
					<div class="sidebar-item-control"></div>
				</div>
				<div class="sidebar-child-item nested-container"></div>
			</div>
		`)}};frappe.ui.ThemeSwitcher=class extends frappe.ui.ThemeSwitcher{fetch_themes(){return new Promise(e=>{this.themes=[{name:"InnTheme",label:__("Inn Cyan"),info:__("Inn Cyan")},{name:"InnThemeBlue",label:__("Inn Blue"),info:__("Inn Blue")},{name:"InnThemePeach",label:__("Inn Peach"),info:__("Inn Peach")},{name:"light",label:__("Frappe Light"),info:__("Light Theme")},{name:"dark",label:__("Timeless Night"),info:__("Dark Theme")},{name:"automatic",label:__("Automatic"),info:__("Uses system's theme to switch between light and dark mode")}],e(this.themes)})}};})();
//# sourceMappingURL=inn_theme_desk.bundle.YCUNPN3U.js.map
