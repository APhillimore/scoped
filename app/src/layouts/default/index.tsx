import { Link, Outlet } from "react-router-dom";

export default function DefaultLayout() {
	return (
		<>
			<header>
				<h1>Scoped</h1>
				<nav>
					<Link to="/">Home</Link>
					<Link to="/projects">Projects</Link>
				</nav>
			</header>
			<Outlet />
		</>
	);
}
