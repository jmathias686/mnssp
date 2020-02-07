import React, { Component } from 'react'

export class Attendance extends Component {
    constructor(props){
        super(props);
        this.state = {
          list: {}
        }
      }

    async componentDidMount() {
        const url = "http://localhost:5000/Users/attending";
        const response = await fetch(url);
        const data = await response.json();
        this.setState({list : data});
    }

    render() {
        return (
            <div>
                {/* JSON.stringify({this.state.list}) */}
            </div>
        )
    }
}

export default Attendance
