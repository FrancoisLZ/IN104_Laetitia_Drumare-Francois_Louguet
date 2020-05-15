//components/Search.js

import React from 'react';
import { View, TextInput, Button } from 'react-native'

class Search extends React.Component {
  render() {
    return(
      <view style={{ marginTop:20, backgroundColor: 'pink'}}>
          <TextInput style={{ marginLeft: 5, marginRight: 5, height: 50, borderColor: '#000000', borderWidth: 1, paddingLeft: 5 }}  placeholder='lieu de départ'/>
          <Button title='Rechercher' onPress={() => {}}/>
      </view>   
    )
  }
}

export default Search