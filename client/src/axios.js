import React, { Component } from 'react';
import axios from 'axios';
import JSONPretty from 'react-json-pretty';
import JSONPrettyMon  from 'react-json-pretty/dist/monikai';

export default class FastApi extends Component {
  state = {
    seenIndexes: [],
    values: {},
    index: '',
  };

  componentDidMount() {
    axios.get(`http://localhost:8080/`, {
        mode: 'cors',
    })
      .then(res => {
        const response = res.data;
        this.setState({ response });
      })
  }

  render() {

    return (

      <div>
        <JSONPretty data={this.state.response} theme={JSONPrettyMon} themeClassName="json__class" mainStyle={{backgroundColor: "#282c34"}}></JSONPretty>
      </div>

    );
  }
}

