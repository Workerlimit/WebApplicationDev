import React, { Component } from 'react';

const withAuthentication = (WrappedComponent) => {
    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {
                isAuthenticated: false,
            };
        }

        componentDidMount() {
            setTimeout(() => {
                this.setState({ isAuthenticated: true });
            }, 2000);
        }

        render() {
            if (!this.state.isAuthenticated) {
                return <p>Please log in to access this content.</p>;
            }

            return <WrappedComponent {...this.props} />;
        }
    };
};

export default withAuthentication;
