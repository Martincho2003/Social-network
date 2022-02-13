import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import axios from "axios";

const api = axios.create({
	baseURL: 'http://127.0.0.1:8000/chats/register'
})

class SignUp extends Component {

	constructor(props) {
    super(props);
    this.state = {
      firstName: '',
      secondName: '',
      email: '',
      password1: '',
      password2: '',
      redirect: null,
      is_failed: null,
    };

    this.handleFirstName = this.handleFirstName.bind(this);
    this.handleSecondName = this.handleSecondName.bind(this);
    this.handleEmail = this.handleEmail.bind(this);
    this.handlePassword1 = this.handlePassword1.bind(this);
    this.handlePassword2 = this.handlePassword2.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleFirstName(event) {
    this.setState({firstName: event.target.value});
  }
  handleSecondName(event) {
    this.setState({secondName: event.target.value});
  }
  handleEmail(event) {
    this.setState({email: event.target.value});
  }
  handlePassword1(event) {
    this.setState({password1: event.target.value});
  }
  handlePassword2(event) {
    this.setState({password2: event.target.value});
  }

  handleSubmit(event) {
    //console.log(this.state);

    this.createUser();
    event.preventDefault();
  }

	createUser = async () => {
		let res = await api.post('/', {first_name: this.state.firstName, last_name: this.state.secondName, email: this.state.email, password: this.state.password1, username: this.state.firstName, is_active: true })
    
    /*
    //if the backend says no render "Oops something went wrong" log in the form
    if (res "not good???" ){
      this.setState({is_failed: <label className="red_label" >Oops something went wrong </label>});
    }else{
      this.setState({redirect: <Redirect to="/login" />});
    }
    */

		//console.log(res);
    this.setState({is_failed: <label className="red_label" >Oops something went wrong </label>});

	}

  render() {
    
		return (
			<div className="auth-wrapper form_body">
				<div className="auth-inner">
					<form onSubmit={this.handleSubmit}>
						<h3>Sign Up</h3>
            {this.state.is_failed}
						<div className="form-group">
							<label>First name</label>
							<input type="text" className="form-control" placeholder="First name" value={this.state.firstName} onChange={this.handleFirstName}/>
						</div>
						<div className="form-group">
							<label>Last name</label>
							<input type="text" className="form-control" placeholder="Last name" value={this.state.secondName} onChange={this.handleSecondName}/>
						</div>
						<div className="form-group">
							<label>Email address</label>
							<input type="email" className="form-control" placeholder="Enter email" value={this.state.email} onChange={this.handleEmail}/>
						</div>
						<div className="form-group">
							<label>Password</label>
							<input type="password" className="form-control" placeholder="Enter password" value={this.state.password1} onChange={this.handlePassword1}/>
						</div>
            {/*  
            <div className="form-group">
							<label>Confirm Password</label>
							<input type="password" className="form-control" placeholder="Confirm password" value={this.state.password2} onChange={this.handlePassword2}/>
						</div>
            */}
						<button type="submit" className="btn btn-primary btn-block">Sign Up</button>
						<p className="forgot-password text-right">
							Already registered <Link to="/login">sign in?</Link>
						</p>
					</form>
          {this.state.redirect}
				</div>
			</div>
		);
	}
}

export default SignUp;