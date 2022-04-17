import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import { BrowserRouter, Route } from 'react-router-dom';

import SignIn from "./components/SignIn";
import SignUp from "./components/SignUp";
import Chats from "./components/Chats";
import SuccessSignUp from "./components/SuccessSignUp";
import DirectMessaging from './components/DirectMessaging';

const routes = (
  <BrowserRouter>
    <Route path="/signin">
      <SignIn />
    </Route>
    <Route path="/signup">
      <SignUp />
    </Route>
    <Route path="/bad_chats">
      <Chats />
    </Route>
    <Route path="/success">
      <SuccessSignUp />
    </Route>
    <Route path="/chats">
      <DirectMessaging />
    </Route>
  </BrowserRouter>
);

const rootElement = document.getElementById("root");
ReactDOM.render(routes, rootElement);
