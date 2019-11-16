import React, { Component } from 'react';
import { View, Button, Text } from 'react-native';
import * as Facebook from 'expo-facebook';
import axios from 'axios';
import EventListView from './EventListView';

export default class LoginView extends Component {
  login = async () => {
    try {
      const {
        type,
        token,
        expires,
        permissions,
        declinedPermissions,
      } = await Facebook.logInWithReadPermissionsAsync('981730282184579', {
        permissions: ['public_profile', 'email', 'user_hometown', 'user_likes', 'user_link'],
      });
      if (type === 'success') {
        const response = await axios(`https://graph.facebook.com/me?access_token=${token}`);
        alert(`Hi ${response.data.name}, welcome to Facebook IRL!`);
        this.setState({ login: response.data });
      } else {
        alert('Login cancelled :(')
      }
    } catch ({ message }) {
      alert(`Facebook Login Error: ${message}`);
    }
  }

  render() {
    return (
      this.state.login ?
        <EventListView /> :
        <View style={{
          flex: 1,
          justifyContent: 'center',
          alignItems: 'center'
        }}>
          <Text style={{ fontSize: 40 }}>Login to Facebook</Text>
          <Text style={{ fontSize: 20, marginBottom: 20 }}>to access premiere events near you!</Text>
          <Button style={{ borderRadius: 40 }} onPress={async () => await this.login()} title="Login to Facebook!" />
        </View>
    );
  }
};

module.exports = LoginView;