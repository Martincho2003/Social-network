<<<<<<< HEAD
import React, { Component } from "react";
import axios from "axios";

const api = axios.create({
	baseURL: 'http://127.0.0.1:8000/chats/api/chats/'
})

class App extends Component {

	state = {
		chats: []
	}

	constructor(){
		super();
		this.getChats();
	}

	getChats = async () => {
		let data = await api.get('/').then(({ data }) => data);
			
		this.setState({chats: data})
	}

	createChat = async () => {
		let res = await api.post('/', {chat_name: "added_with Axios", chat_owner: 1, chat_members_count: 2})

		console.log(res)
		this.getChats();
	}

	deleteChat = async (id) => {
		let data = await api.delete(`/${id}/`)

		console.log(data)
		this.getChats();
	}

	updateChat = async (id, val) => {
		let data = await api.patch(`/${id}/`, {chat_name : val})

		console.log(data)
		this.getChats();
	}

	render() {
		return (
			<div>
				<button onClick={this.createChat}>create chat</button>
				
				{this.state.chats.map(chat => 
					<h2 key={chat.id} onClick={() => this.updateChat(chat.id, chat.chat_name + "a")}>
						{chat.chat_name}
						<button onClick={() => this.deleteChat(chat.id)}>x</button>
					</h2>
				)}
			</div>
		);
	}
}

export default App;
=======
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
>>>>>>> master
