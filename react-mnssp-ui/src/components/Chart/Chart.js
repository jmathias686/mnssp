import React, { Component } from 'react'
import {Bar} from "react-chartjs-2";


class Chart extends Component {

    constructor(props){
        super(props);
        this.state = {
          chartData:props.chartData
        }
      }

    static defaultProps= {
        displayTitle:false,
    }

    render() {
        return (
            <div className="chart">
                <h1>Votes for Movie Night</h1>
                <Bar
                    data = {this.state.chartData}
                    options={{
                        title: {
                            display: this.props.displayTitle,
                            text: 'Votes for Movie Night',
                            fontSize: 25
                        }
                    }}
                />
            </div>
        )
    }
}
 
export default Chart
