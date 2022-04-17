import React, { Component } from "react";
import { Redirect, BrowserRouter, Route } from "react-router-dom";
import axios from "axios";

const api = axios.create({
	baseURL: 'http://127.0.0.1:8000/chats/login'
})

class SignIn extends Component {

	constructor(props) {
		super(props);
		this.state = {
		  username: '',
		  password: '',
		  result: '',
		  redirect: null,
      	  is_failed: null,
		};

		this.handleUsername = this.handleUsername.bind(this);
		this.handlePassword = this.handlePassword.bind(this);

		this.handleSubmit = this.handleSubmit.bind(this);
	  }

	  handleUsername(event) {
		this.setState({username: event.target.value});
	  }
	  handlePassword(event) {
		this.setState({password: event.target.value});
	  }
	
	  handleSubmit(event) {
		//console.log(this.state);
	
		this.checkUser();
		event.preventDefault();
	  }

	  checkUser = async () => {
		console.log(this.state.username);
		let res = await api.post('', { username: this.state.username, password: this.state.password});
		console.log(res.data.status);
		
		//if the backend says no render "Oops something went wrong" log in the form
		if (res.data.status == "unsuccessful"){
			this.setState({is_failed: <label className="red_label" >Oops something went wrong </label>});
		}else{
			this.setState({redirect: <Redirect to="/chats" />});
		}
	}

  render() {
		return (
			<div className="auth-wrapper form_body">
				<div className="auth-inner">
					<form onSubmit={this.handleSubmit}>
						<h3>Sign In</h3>
						{this.state.is_failed}
						<div className="form-group">
							<label>Username</label>
							<input type="text" className="form-control" placeholder="Enter username" value={this.state.username} onChange={this.handleUsername}/>
						</div>
						<div className="form-group">
							<label>Password</label>
							<input type="password" className="form-control" placeholder="Enter password" value={this.state.password} onChange={this.handlePassword}/>
						</div>
						{/*
						<div className="form-group">
							<div className="custom-control custom-checkbox">
								<input type="checkbox" className="custom-control-input" id="customCheck1" />
								<label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
							</div>
						</div>
						*/}
						<button type="submit" className="btn btn-primary btn-block">Submit</button>
						{/*
						<p className="forgot-password text-right">
							Forgot <a href="#">password?</a>
						</p>
						*/}
					</form>
					{this.state.redirect}
				</div>
			</div>
			
		);
	}
}

export default SignIn;