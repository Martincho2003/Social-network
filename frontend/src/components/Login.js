import React, { Component } from "react";
import { Redirect, BrowserRouter, Route } from "react-router-dom";
import axios from "axios";

const api = axios.create({
	baseURL: 'http://127.0.0.1:8000/chats/api/users/' // replace this with the addres of the django handler
})

class Login extends Component {

	constructor(props) {
		super(props);
		this.state = {
		  email: '',
		  password: '',
		  result: '',
		  redirect: null,
      	  is_failed: null,
		};

		this.handleEmail = this.handleEmail.bind(this);
		this.handlePassword = this.handlePassword.bind(this);

		this.handleSubmit = this.handleSubmit.bind(this);
	  }

	  handleEmail(event) {
		this.setState({email: event.target.value});
	  }
	  handlePassword(event) {
		this.setState({password: event.target.value});
	  }
	
	  handleSubmit(event) {
		console.log(this.state);
	
		this.checkUser();
		event.preventDefault();
	  }

	  checkUser = async () => {
		let res = await api.get('/', { email: this.state.email, password: this.state.password})
		
		/*
		//if the backend says no render "Oops something went wrong" log in the form
		if (res "not good???" ){
		this.setState({is_failed: <label className="red_label" >Oops something went wrong </label>});
		}else{
		this.setState({redirect: <Redirect to="/chats" />});
		}
		*/

		console.log(res);
		this.setState({redirect: <Redirect to="/chats" />});
	}

  render() {
		return (
			<div className="auth-wrapper form_body">
				<div className="auth-inner">
					<form onSubmit={this.handleSubmit}>
						<h3>Sign In</h3>
						{this.state.is_failed}
						<div className="form-group">
							<label>Email address</label>
							<input type="email" className="form-control" placeholder="Enter email" />
						</div>
						<div className="form-group">
							<label>Password</label>
							<input type="password" className="form-control" placeholder="Enter password" />
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

export default Login;