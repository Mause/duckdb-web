function GenerateDownloadUrl() {
	return DiagramNode(Stack([
        Sequence([
            "http://extensions.duckdb.org/",
			Group(
				Choice(0, ["v0.6.2-dev60", "v0.6.1", "v0.6.0"]),
				'Version'
			),
            "/"
        ]),
        Sequence([
            Group(
                Sequence([
                    Choice(0, ["linux", "windows", "osx"]), "_",
                    Choice(0, ["amd64", "i386", "arm64"]),
                    Optional("_gcc4"),
                ]),
                "Platform String",
            ),
            "/",
        ]),
        Sequence([
			Group(
				Choice(0, ["arrow", "httpfs", "sqlite_scanner", "..."]),
				'Extension name',
			),
            ".duckdb_extension.gz"
        ])
    ]));
}

function Initialize(options = {}) {
	let generateAggregate = GenerateDownloadUrl(options);
	let element = document.getElementById("rrdiagram");
	element.classList.add("limit-width");
	element.innerHTML = generateAggregate.toString();

}

function Refresh(node_name, set_node) {
	options[node_name] = set_node;
	Initialize(options);
}

options = {}

window.addEventListener('load', Initialize);

