import { useEffect, useState } from "react";

export default function Projects() {
	const [projects, setProjects] = useState([]);
	useEffect(() => {
		fetch("http://localhost:8000/v1/projects/")
			.then((response) => response.json())
			.then((data) => setProjects(data));
	}, []);
	return (
		<div>
			<h1>Projects</h1>
			{projects.map((project) => (
				<div key={project.id}>{project.name}</div>
			))}
		</div>
	);
}
