import React from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import TitleCard from './titleCard'
import Player from './player'
import Header from './header'

function Index() {
	return (
		<div>
			<TitleCard />
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
				<Header />

				<Route path="/" exact component={Index} />
				<Route path="/about" component={About} />
				<Route path="/music" component={Music} />
			</div>
		</Router>
	);
}

export default AppRouter;

