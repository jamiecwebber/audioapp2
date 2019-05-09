import React, { Component } from 'react';
// import ReactDOM from 'react-dom';
import './header.css'
import logo from './images/fox-logo.jpg'

class Header extends Component {
	render () {
		return (
			<div id='header'>
				<div className="headerSections"><img className='logo' src={logo} alt=''/> <h1>Red Vixen Music</h1><h2> - projects of Jamie Christopher Webber</h2></div>
				<div className="headerSections"><h2>web development</h2><h2>composition</h2><h2>audio programming</h2></div>
			</div>
		)
	}
}

export default Header