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
        displayTitle:true,
    }

    render() {
        return (
            <div className="chart">
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
