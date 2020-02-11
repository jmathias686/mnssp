import React, { Component } from 'react'

export class Attendance extends Component {
    constructor(props){
        super(props);
        this.state = {
          list: {}
        }
      }

    async componentDidMount() {
        const url = "http://localhost:5000/Users/attendee";
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
        this.setState({list : data});
    }
    
    render() {
        var json = this.state;
        return (
            <div>
                <pre>{JSON.stringify(json, null, 2)}</pre>
                Hello
            </div>
        )
    }
}

export default Attendance
