import React, { Component } from 'react'
import NavBar from './components/NavBar/NavBar'
import Routes from './components/Routes'
// import SignIn from './components/SignIn/SignIn'
// import ButtonRouter from './ButtonRouter'
// import history from './components/history'
import Copyright from './components/Copyright/Copyright'
import Box from '@material-ui/core/Box';


class App extends Component {
  render() {
    return (
      <div>
        <NavBar />
        {/* <ButtonRouter /> */}
        <Routes />
        <Box mt={5}>
          <Copyright />
        </Box>
      </div>
    );
  }
}
export default App