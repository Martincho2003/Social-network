import React, { Component, useState} from "react";
import axios from "axios";


const chatsList = axios.create({
	baseURL: 'http://127.0.0.1:8000/chats/chats-list'
})

class Chats extends Component {

	state = {
		chats: []
	}

	constructor(props){
		super();
		this.getChats();
	}

	getChats = async () => {
		console.log(localStorage.getItem('username'))
		let data = await chatsList.get('', {params: { username: 'marti'}}).then(({ data }) => data);
		console.log(data);
	}

	// createChat = async () => {
	// 	let res = await api.post('/', {chat_name: "added_with Axios", chat_owner: 1, chat_members_count: 2})

	// 	console.log(res)
	// 	this.getChats();
	// }

	// deleteChat = async (id) => {
	// 	let data = await api.delete(`/${id}/`)

	// 	console.log(data)
	// 	this.getChats();
	// }

	// updateChat = async (id, val) => {
	// 	let data = await api.patch(`/${id}/`, {chat_name : val})

	// 	console.log(data)
	// 	this.getChats();
	// }

	render() {

		return (
			<div>
				{/* <button onClick={this.createChat}>create chat</button>
				
				{this.state.chats.map(chat => 
					<h2 key={chat.id} onClick={() => this.updateChat(chat.id, chat.chat_name + "a")}>
						{chat.chat_name}
						<button onClick={() => this.deleteChat(chat.id)}>x</button>
					</h2>
				)} */}
				
			</div>
		);
	}
}

export default Chats;