import React, { Component } from 'react'
import Typography from '@material-ui/core/Typography'
import Chart from 'chart.js';
import Grid from '@material-ui/core/Grid'
import Box from '@material-ui/core/Box'

export class Poll extends Component {
    state = {
        loading: true,
        poll: null,
    }

    // data: {
    //     datasets: [{
    //         barPercentage: 0.5,
    //         barThickness: 6,
    //         maxBarThickness: 8,
    //         minBarLength: 2,
    //         data: [1, 2]
    //     }]d
    // };


    async componentDidMount() {
        const url = "http://localhost:5000/Poll/";
        const response = await fetch(url);
        const data = await response.json();
        data[0].count = 7;
        data[1].count = 4;
        this.setState({poll: data, loading: false});
        console.log(this.state.poll);
    }

    render() {
        return (
            <div>
                {this.state.loading || !this.state.poll ?
                    <div>loading...</div>
                :
                    <Box>
                        <Typography variant = "h4">Poll Data</Typography>
                        <div>{this.state.poll[0].movie_title}</div>
                        <Typography variant = "body2">votes = {this.state.poll[0].count}</Typography>
                    </Box>
                    // <Box>
                    //     <Typography variant = "h4">Poll Data</Typography>
                    //     <div>{this.state.poll[1].movie_title}</div>
                    //     <Typography variant = "body2">votes = {this.state.poll[1].count}</Typography>
                    // </Box>
                }
            </div>
        )
    }
}

export default Poll
