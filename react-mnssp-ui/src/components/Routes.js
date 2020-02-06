import React, { Component } from "react";
import { Router, Switch, Route, Redirect } from "react-router-dom";

import SignIn from "./SignIn/SignIn";
import SignUp from "./SignUp/SignUp";
import Poll from "./Poll"
// import LandingPage from "./LandingPage/LandingPage";
import history from './history';

export default class Routes extends Component {
    render() {
        return (
            
            <Router history={history}>
                <Switch>
                    <Route exact path="/">
                        <SignIn />
                    </Route>
                    <Route path="/SignUp">
                        <SignUp />
                    </Route>
                    <Route path="/Poll">
                        <Poll />
                    </Route>
                </Switch>
            </Router>
        )
    }
}