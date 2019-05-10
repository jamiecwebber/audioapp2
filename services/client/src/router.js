import React from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import TitleCard from './titleCard'
import Player from './player'

function Index() {
	return (
		<div>
			<TitleCard />
			<Player />
		</div>
	);
}

function About() {
	return <h2>About</h2>;
}

function Music() {
	return <h2>Sounds</h2>;
}

function AppRouter() {
	return (
		<Router>
			<div>
				<nav>
					<ul>
						<li>
							<Link to="/">Home</Link>
						</li>
						<li>
							<Link to="/about/">About</Link>
						</li>
						<li>
							<Link to="/music/">Music</Link>
						</li>
					</ul>
				</nav>

				<Route path="/" exact component={Index} />
				<Route path="/about" component={About} />
				<Route path="/music" component={Music} />
			</div>
		</Router>
	);
}

export default AppRouter;

