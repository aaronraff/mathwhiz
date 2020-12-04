import React from 'react';
import Challenge from "./Challenge"
import Home from "./Home"
import Nav from "./Nav"
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from "react-router-dom";

function App() {
  return (
    <>
      <Nav />
      <Router>
        <Switch>
          <Route exact={true} path="/" component={Home} />
          <Route exact={true} path="/challenge/:joinCode" component={Challenge} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
