
oCCDB = {
	["profileKeys"] = {
		{%- for character in account.characters %}
		["{{ character.titled_character_name }} - {{ character.realm_name }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["tscd"] = {
				["lock"] = true,
				["enable"] = false,
			},
			["notify"] = {
				["scale"] = 0.5,
				["y"] = 259.1017037928452,
				["x"] = 468.5910979920071,
				["lock"] = true,
			},
		},
	},
}
