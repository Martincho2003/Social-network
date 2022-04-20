import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useNavigate } from 'react-router';
import { useState, useEffect } from 'react';
import Login from "./components/Login";
import SignUp from "./components/SignUp";
import OldChats from "./components/OldChats";
import Chats from "./components/Chats";
import SuccessSignUp from "./components/SuccessSignUp";

function App() {
  let applicationState = JSON.parse(localStorage.getItem('appState'))
  if (!applicationState) {
    applicationState = {
        username: ''
    }
  }
  
  const [appState, setAppState] = useState(applicationState);
  const navigate = useNavigate();
  const name = localStorage.getItem('username');

  useEffect(() => {
    if (!name) {
      navigate('/login');
    }
    localStorage.setItem('appState', JSON.stringify(appState)); 
  }, [appState]);

  //localStorage.clear();

  return (
    <Routes>
        <Route path="/login" element={<Login appState={appState} setAppState={setAppState}/>} />
        <Route path="/signup" element={<SignUp appState={appState} setAppState={setAppState}/>} />
        <Route path="/oldchats" element={<OldChats appState={appState} setAppState={setAppState}/>} />
        <Route path="/chats" element={<Chats appState={appState} setAppState={setAppState}/>} />
        <Route path="/success" element={<SuccessSignUp appState={appState} setAppState={setAppState}/>} />
    </Routes>
  );
}

export default App;