import React, { Component, Fragment } from 'react'

export default class Maincontent extends Component {
    render() {
        return (
            <Fragment>
                id = {this.props.id}
                <br />
                {this.props.body}
                <br />
                <hr />
            </Fragment>
        )
    }
}

