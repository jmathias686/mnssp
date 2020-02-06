import React, { Component } from 'react'
// import Typography from '@material-ui/core/Typography'
// import Grid from '@material-ui/core/Grid'
// import Box from '@material-ui/core/Box'
import Chart from './Chart/Chart'

export class Poll extends Component {
    state= {
        loading:true,
        poll:null,
        chartData:{}
    }

    random_rgba() {
        return 'rgba(' + String(Math.floor(Math.random() * 256)) + ',' + String(Math.floor(Math.random() * 256)) + ',' + String(Math.floor(Math.random() * 256)) + ', 0.6)';
    }


    // backgroundColor = [this.random_rgba()];

    background_Color(data) {
        var colours = [];
        var i;
        for (i = 0; i <  data.length; i++) {
            colours.push(this.random_rgba());
        }
        return colours
    }
    
    newState(data) {
        this.setState({
            poll: data,
            loading: false,
            chartData: {
                labels: ['Bad Boys for Life', '1917', 'something', 'frozen II'],
                datasets:[
                    {
                    label: 'Movie Title',
                    data: [7,2,4,3,0],  //NEED TO HAVE 0 APPENDED ON THE END TO SCALE TO 0
                    barPercentage: 0.5,
                    barThickness: 40,
                    maxBarThickness: 40,
                    minBarLength: 2,
                    backgroundColor: this.background_Color(data)
                }]
            },
        })
    }

    async componentDidMount() {
        const url = "http://localhost:5000/Poll/";
        const response = await fetch(url);
        const data = await response.json();
        data[0].count = 7;
        data[1].count = 4;
        this.newState(data);
        console.log(this.state.chartData)
        console.log(this.state.poll);
    }

    render() {
        return (
            <div>
                {this.state.loading || !this.state.poll || !this.state.chartData ?
                    <div>loading...</div>
                :
                    <Chart chartData={this.state.chartData}/>
                }
            </div>
            
        )
    }
}

export default Poll
