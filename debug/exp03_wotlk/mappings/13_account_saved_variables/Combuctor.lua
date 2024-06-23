
CombuctorDB2 = {
	["global"] = {
		["maxScale"] = 1.5,
	},
	["version"] = "2.2.2",
	["profiles"] = {
		{%- for character in account.characters %}
		["{{ character.titled_character_name }} - {{ character.realm_name }}"] = {
			["inventory"] = {
				["exclude"] = {
					["All"] = {
						"All", -- [1]
						"Ammo", -- [2]
					},
				},
				["h"] = 658.1035050443454,
				["position"] = {
					"RIGHT", -- [1]
					nil, -- [2]
					"RIGHT", -- [3]
					-46.85336921019098, -- [4]
					-43.03211348506775, -- [5]
				},
				["showBags"] = false,
				["sets"] = {
					"全部", -- [9]
					"装备", -- [10]
					"消耗品", -- [11]
					"任务", -- [12]
					"商品", -- [13]
					"弹药", -- [14]
					"其它", -- [15]
				},
				["bags"] = {
					-2, -- [1]
					0, -- [2]
					1, -- [3]
					2, -- [4]
					3, -- [5]
					4, -- [6]
				},
				["w"] = 731.4488696991256,
				["leftSideFilter"] = true,
			},
			["bank"] = {
				["h"] = 512,
				["showBags"] = false,
				["sets"] = {
					"All", -- [1]
					"Equipment", -- [2]
					"Trade Goods", -- [3]
					"Miscellaneous", -- [4]
					"Usable", -- [5]
					"Quest", -- [6]
					"Projectile", -- [7]
					"Soul Shard", -- [8]
				},
				["bags"] = {
					-1, -- [1]
					5, -- [2]
					6, -- [3]
					7, -- [4]
					8, -- [5]
					9, -- [6]
					10, -- [7]
					11, -- [8]
				},
				["w"] = 512,
				["exclude"] = {
					["All"] = {
						"All", -- [1]
						"Shards", -- [2]
						"Ammo", -- [3]
						"Keys", -- [4]
					},
				},
			},
		},
		{%- endfor %}
	},
}
CombuctorVersion = nil
