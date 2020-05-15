import React, { PureComponent } from 'react';
import { StyleSheet, View } from 'react-native';

type PropsType = {};

export default class Nickname extends PureComponent<PropsType> {
  render() {
    return (
      <View/>
    );
  }
}

const styles = StyleSheet.create({
  nicknameLine: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: theme.margin,
  },
  nickname: {
    ...theme.typo.title,
    marginLeft: 2 * theme.margin,
    marginRight: theme.margin,
    color: theme.colors.white,
  },
});