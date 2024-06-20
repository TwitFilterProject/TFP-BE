import { Injectable } from '@nestjs/common';
import FB from 'fb';
import * as fs from 'fs';
import * as path from 'path';
import axios from 'axios';
import { findSourceMap } from 'module';

@Injectable()
export class AppService {
  fbAccessToken: string;

  constructor() {
    this.fbAccessToken = 'EAAb6aDIUTLcBO7cEXKO59HaXzRN4Yecw3taYszsxEkb9Ke42uVZChP7ZBTJXkTDidq7kZAFY7yQRCyH9mZCwCih0968K9VKRXtH3ZBH2TZCAlGqGMZC30DRjxMzavzXc4cQmxE91ghT1UhRYaQLNZBetMBJHLKm63Kz5DZCsOAzZBJ3PGZBUKZALiVNvHyzsa7cKwWcdLCxv3MK4'
    FB.setAccessToken(this.fbAccessToken);
  }

  async getFeed(): Promise<any> {
    const feedArr = await FB.api(
      '/325237764009663/feed',
      'GET',
      {},
    );

    console.log(feedArr.data)

    const finalArr = [];

    for(const feed of feedArr.data) {
      const body = feed.message;
      console.log(body)
      const {data} = await axios.post('http://127.0.0.1:9001/bertHate', {body});
      console.log(data)
      const indicesWithOnes = data
      .map((value: number, index: any) => (value === 1 ? index : -1))
      .filter(index => index !== -1);
      
      console.log(indicesWithOnes)
      if(indicesWithOnes.includes(8)) {
        finalArr.push(body)
      }else {
        finalArr.push("혐오 발언을 포함하고 있는 문장입니다.")
      }
    }

    return finalArr;

    // const facebookFeed = new Promise((resolve, reject) => {
    //   FB.api(
    //     '/325237764009663/feed',
    //     'GET',
    //     {},
    //     async function(response: any) {
    //       if (response && !response.error) {
    //         const {data} = await axios.post('http://127.0.0.1:9001/bertHate', {response});
    //         if(data == "0") {
    //           resolve(response.data);
    //         }else {
    //           resolve("혐오 발언이 포함된 문장입니다.")
    //         }
    //       } else {
    //         reject(response.error);
    //       }
    //     }
    //   );
    // });
    // for(const feed of facebookFeed) {

    // }
  }

  async getImage(): Promise<void> {
    const body = '.';
    const {data} = await axios.post('http://127.0.0.1:9002/imageClassification', {body});
    return data;
  }
}

// /accounts?fields=name,access_token&access_token=
// /accounts?fields=about,attire,bio,location,parking,hours,emails,website&access_token=

// PAGE-ID/insights?metric=page_messages_new_conversations_unique,page_messages_blocked_conversations_unique&access_token=PAGE-ACCESS-TOKEN"