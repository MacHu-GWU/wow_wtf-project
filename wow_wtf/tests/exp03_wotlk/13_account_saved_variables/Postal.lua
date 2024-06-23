
Postal3DB = {
	["global"] = {
		["BlackBook"] = {
			["alts"] = {
			},
		},
	},
	["profileKeys"] = {
		{%- for character in account.characters %}
		["{{ character.titled_character_name }} - {{ character.realm_name }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["BlackBook"] = {
				["recent"] = {
					{%- for character in account.characters %}
					"{{ character.titled_character_name }}",
					{%- endfor %}
				},
			},
		},
	},
}
