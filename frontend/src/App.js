import React, { Component } from "react";
import { BrowserRouter, Link, Route, Switch } from 'react-router-dom';
import axios from "axios";

import Login from "./components/Login/Login";
import Whale from "./components/Whale/Whale";
import Chats from "./components/Chats/Chats";

const api = axios.create({
	baseURL: 'http://127.0.0.1:8000/chats/api/chats/'
})

class App extends Component {

	render() {
		return (
			<div>
				<BrowserRouter>
				<Switch>
					<Route path="/">
						<Login />
					</Route>
					<Route path="/whale">
						<Whale />
					</Route>
					<Route path="/chats">
						<Chats />
					</Route>
					
					</Switch>
				</BrowserRouter>
			</div>
		);
	}
}

export default App;