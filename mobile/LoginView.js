import React, {Component} from 'react';
import {View, Button, Text, Image} from 'react-native';
import * as Facebook from 'expo-facebook';
import axios from 'axios';
import EventListView from './EventListView';

export default class LoginView extends Component {
    state = {};

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
                this.setState({login: response.data});
            } else {
                alert('Login cancelled :(')
            }
        } catch ({message}) {
            alert(`Facebook Login Error: ${message}`);
        }
    }

    render() {
        return (
            this.state.login ?
                <EventListView/> :
                <View style={{
                    flex: 1,
                    justifyContent: 'center',
                    alignItems: 'center',
                    backgroundColor: '#3b5998'
                }}>
                    <Image source={require('./assets/logo.png')} style={{width: 200, height: 200, marginBottom: 100}}/>
                    <Text style={{fontSize: 18, marginBottom: 20, color: 'white', fontfamily: 'Roboto'}} >
                        The AR social network for real connections.
                    </Text>
                    <Button
                        style={{
                            borderWidth: 1,
                            borderColor: 'rgba(0,0,0,0.2)',
                            alignItems: 'center',
                            justifyContent: 'center',
                            width: 150,
                            height: 150,
                            borderRadius: 150,
                            fontFamily: 'Roboto'
                        }}
                        color={'#f7f7f7'}
                        title={'Continue with Facebook'}
                        onPress={async () => await this.login()}
                    />
                </View>
        );
    }
};

module.exports = LoginView;