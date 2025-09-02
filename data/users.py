from datetime import datetime, timedelta

FAKE_USERS = [
	{
		"name": "Zara Ahmed",
		"avatar": "👩‍🔬",
		"interests": ["Biotechnology", "Genomics", "Research"],
		"current_activity": "Analyzing CRISPR off-target effects",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=2)).isoformat()
	},
	{
		"name": "Kai Nakamura",
		"avatar": "👨‍🎮",
		"interests": ["Game Dev", "Unity", "C#"],
		"current_activity": "Prototyping a VR puzzle mechanic",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=7)).isoformat()
	},
	{
		"name": "Sofia Rodriguez",
		"avatar": "👩‍💼",
		"interests": ["Fintech", "Blockchain", "DeFi"],
		"current_activity": "Designing smart contract audits",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=4)).isoformat()
	},
	{
		"name": "Alex Thompson",
		"avatar": "👨‍🎨",
		"interests": ["Digital Art", "NFTs", "Creative Tech"],
		"current_activity": "Rendering a generative art series",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=11)).isoformat()
	},
	{
		"name": "Priya Sharma",
		"avatar": "👩‍⚕️",
		"interests": ["Healthcare AI", "Radiology", "Data Science"],
		"current_activity": "Training a chest X-ray classifier",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=1)).isoformat()
	},
	{
		"name": "Marcus Johnson",
		"avatar": "👨‍🚀",
		"interests": ["Space Tech", "Robotics", "Aerospace"],
		"current_activity": "Testing rover suspension control",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=9)).isoformat()
	},
	{
		"name": "Lena Chen",
		"avatar": "👩‍🎓",
		"interests": ["Quantum Computing", "Physics", "Math"],
		"current_activity": "Optimizing VQE ansatz depth",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=6)).isoformat()
	},
	{
		"name": "Omar Hassan",
		"avatar": "👨‍🍳",
		"interests": ["Food Tech", "Sustainability", "Bioengineering"],
		"current_activity": "Formulating plant-based protein blends",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=13)).isoformat()
	},
	{
		"name": "Maya Patel",
		"avatar": "👩‍💻",
		"interests": ["Python", "LLMs", "MLOps"],
		"current_activity": "Evaluating RAG pipeline latency",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=3)).isoformat()
	},
	{
		"name": "Diego Alvarez",
		"avatar": "👨‍🔧",
		"interests": ["IoT", "Edge AI", "Electronics"],
		"current_activity": "Soldering a low-power sensor board",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=12)).isoformat()
	},
	{
		"name": "Hannah Kim",
		"avatar": "👩‍🏫",
		"interests": ["EdTech", "Curriculum", "Learning Science"],
		"current_activity": "Designing spaced-repetition modules",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=18)).isoformat()
	},
	{
		"name": "Noah Williams",
		"avatar": "👨‍💼",
		"interests": ["Startup Ideas", "Market Research", "Growth"],
		"current_activity": "Interviewing 5 early adopters",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=5)).isoformat()
	},
	{
		"name": "Aisha Suleiman",
		"avatar": "👩‍🔬",
		"interests": ["Climate", "Carbon Capture", "Policy"],
		"current_activity": "Comparing DAC sorbent efficiencies",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=10)).isoformat()
	},
	{
		"name": "Jonas Müller",
		"avatar": "👨‍💻",
		"interests": ["Rust", "Systems", "Performance"],
		"current_activity": "Profiling async runtime overhead",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=14)).isoformat()
	},
	{
		"name": "Sara Rossi",
		"avatar": "👩‍🎤",
		"interests": ["Music Tech", "DSP", "Generative Audio"],
		"current_activity": "Tuning a diffusion audio model",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=22)).isoformat()
	},
	{
		"name": "Ethan Brown",
		"avatar": "👨‍🌾",
		"interests": ["AgriTech", "Drones", "Computer Vision"],
		"current_activity": "Labeling crop stress imagery",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=16)).isoformat()
	},
	{
		"name": "Nadia Ivanova",
		"avatar": "👩‍💼",
		"interests": ["UX", "Product", "Accessibility"],
		"current_activity": "Running a 5-user usability test",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=8)).isoformat()
	},
	{
		"name": "Bilal Khan",
		"avatar": "👨‍⚖️",
		"interests": ["AI Policy", "Ethics", "Privacy"],
		"current_activity": "Drafting AI governance guidelines",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=25)).isoformat()
	},
	{
		"name": "Julie Martin",
		"avatar": "👩‍💼",
		"interests": ["Marketing", "Content", "SEO"],
		"current_activity": "Outlining a product launch plan",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=6)).isoformat()
	},
	{
		"name": "Arjun Mehta",
		"avatar": "👨‍💻",
		"interests": ["Fullstack", "Next.js", "Postgres"],
		"current_activity": "Implementing row-level security",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=9)).isoformat()
	},
	{
		"name": "Camila Souza",
		"avatar": "👩‍🚒",
		"interests": ["Safety", "Wildfire Tech", "Simulation"],
		"current_activity": "Testing wildfire spread models",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=30)).isoformat()
	},
	{
		"name": "Tomáš Novák",
		"avatar": "👨‍🔬",
		"interests": ["Materials", "Batteries", "Solid-State"],
		"current_activity": "Measuring electrolyte conductivity",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=7)).isoformat()
	},
	{
		"name": "Grace Lee",
		"avatar": "👩‍💻",
		"interests": ["Data Viz", "Altair", "Dashboards"],
		"current_activity": "Building KPI dashboard layouts",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=2)).isoformat()
	},
	{
		"name": "Mohamed El-Sayed",
		"avatar": "👨‍🏭",
		"interests": ["Manufacturing", "Automation", "Robotics"],
		"current_activity": "Calibrating a pick-and-place arm",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=19)).isoformat()
	},
	{
		"name": "Isabella Garcia",
		"avatar": "👩‍⚖️",
		"interests": ["Legal Tech", "Contracts", "NLP"],
		"current_activity": "Extracting clauses with LLMs",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=28)).isoformat()
	},
	{
		"name": "Yusuf Demir",
		"avatar": "👨‍🚀",
		"interests": ["Satellites", "RF", "Comms"],
		"current_activity": "Simulating link budget scenarios",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=21)).isoformat()
	},
	{
		"name": "Helena Schmidt",
		"avatar": "👩‍🔧",
		"interests": ["3D Printing", "CAD", "Prototyping"],
		"current_activity": "Tuning PETG print parameters",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=17)).isoformat()
	},
	{
		"name": "Oluwaseun Adebayo",
		"avatar": "👨‍💼",
		"interests": ["FinOps", "Cloud", "Cost Optimization"],
		"current_activity": "Analyzing S3 lifecycle policies",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=15)).isoformat()
	},
	{
		"name": "Fernanda Lima",
		"avatar": "👩‍🌿",
		"interests": ["Urban Farming", "Hydroponics", "Sensors"],
		"current_activity": "Balancing nutrient solution pH",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=35)).isoformat()
	},
	{
		"name": "Ravi Kumar",
		"avatar": "👨‍💻",
		"interests": ["Django", "APIs", "Auth"],
		"current_activity": "Implementing JWT refresh tokens",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=6)).isoformat()
	},
	{
		"name": "Amira Nassar",
		"avatar": "👩‍🔬",
		"interests": ["Neuroscience", "BCI", "Signal Processing"],
		"current_activity": "Filtering EEG artifacts",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=13)).isoformat()
	},
	{
		"name": "Peter Wang",
		"avatar": "👨‍🏫",
		"interests": ["Math", "Education", "Competitions"],
		"current_activity": "Authoring combinatorics problems",
		"online": False,
		"last_active": (datetime.now() - timedelta(minutes=40)).isoformat()
	},
	{
		"name": "Chiara Bianchi",
		"avatar": "👩‍💻",
		"interests": ["Frontend", "React", "Accessibility"],
		"current_activity": "Refactoring keyboard navigation",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=5)).isoformat()
	},
	{
		"name": "Miguel Torres",
		"avatar": "👨‍🔬",
		"interests": ["Chemistry", "Catalysis", "Green Tech"],
		"current_activity": "Screening catalyst candidates",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=24)).isoformat()
	},
	{
		"name": "Anya Petrova",
		"avatar": "👩‍💻",
		"interests": ["Security", "CTF", "Threat Modeling"],
		"current_activity": "Hardening OAuth flows",
		"online": True,
		"last_active": (datetime.now() - timedelta(minutes=20)).isoformat()
	}
] 