import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import { BrowserRouter, Route } from 'react-router-dom';

import Login from "./components/Login";
import SignUp from "./components/SignUp";
import Chats from "./components/Chats";
import SuccessSignUp from "./components/SuccessSignUp";

const routes = (
  <BrowserRouter>
    <Route path="/login">
      <Login />
    </Route>
    <Route path="/signup">
      <SignUp />
    </Route>
    <Route path="/chats">
      <Chats />
    </Route>
    <Route path="/success">
      <SuccessSignUp />
    </Route>
  </BrowserRouter>
);

const rootElement = document.getElementById("root");
ReactDOM.render(routes, rootElement);
