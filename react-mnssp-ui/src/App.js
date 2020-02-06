import React, { Component } from 'react'
import NavBar from './components/NavBar/NavBar'
import Routes from './components/Routes'
// import SignIn from './components/SignIn/SignIn'
// import history from './components/history'
import Copyright from './components/Copyright/Copyright'
import Box from '@material-ui/core/Box';
// import Poll from './components/Poll'


class App extends Component {
  render() {
    return (
      <div>
        <NavBar />
        <Routes />
        <Box mt={5}>
          <Copyright />
        </Box>
        {/* <Poll /> */}
      </div>
    );
  }
}
export default App