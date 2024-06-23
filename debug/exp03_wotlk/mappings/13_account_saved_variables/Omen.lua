
Omen3DB = {
	["profileKeys"] = {
		{%- for character in account.characters %}
		["{{ character.titled_character_name }} - {{ character.realm_name }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["PositionW"] = 221.3526654029161,
			["PositionH"] = 103.351286852943,
			["VGrip2"] = 127.2777944450514,
			["PositionY"] = 341.0580044836042,
			["Locked"] = true,
			["Shown"] = true,
			["ShowWith"] = {
				["Alone"] = true,
			},
			["VGrip1"] = 94.07489154634233,
			["PositionX"] = 1447.858271549452,
		},
	},
}
