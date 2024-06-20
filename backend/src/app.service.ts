import { Injectable } from '@nestjs/common';
import FB from 'fb';

@Injectable()
export class AppService {
  fbAccessToken: string;

  constructor() {
    this.fbAccessToken = 'EAAb6aDIUTLcBO7cEXKO59HaXzRN4Yecw3taYszsxEkb9Ke42uVZChP7ZBTJXkTDidq7kZAFY7yQRCyH9mZCwCih0968K9VKRXtH3ZBH2TZCAlGqGMZC30DRjxMzavzXc4cQmxE91ghT1UhRYaQLNZBetMBJHLKm63Kz5DZCsOAzZBJ3PGZBUKZALiVNvHyzsa7cKwWcdLCxv3MK4'
    FB.setAccessToken(this.fbAccessToken);
  }

  getFeed(): Promise<any> {
    return new Promise((resolve, reject) => {
      FB.api(
        '/325237764009663/feed',
        'GET',
        {},
        function(response: any) {
          if (response && !response.error) {
            resolve(response.data);
          } else {
            reject(response.error);
          }
        }
      );
    });
  }

  // getAlbum(): Promise<any> {
  //   return new Promise((resolve, reject) => {
  //     FB.api('325237764009663/albums', 'GET', {}, (response) => {
  //       if (response && !response.error) {
  //         resolve(response.data);
  //       } else {
  //         reject(response.error);
  //       }
  //     });
  //   });
  // }

  // getPhoto(): any {
  //   const album = this.getAlbum();
  //   FB.api(
  //     '/122104603616345521/picture',
  //     'GET',
  //     {},
  //     function(response) {
  //         // Insert your code here
  //     }
  //   );
  // }


  // 채팅 관련
  // sendChat(): Promise<any> {

  // }
}

// /accounts?fields=name,access_token&access_token=
// /accounts?fields=about,attire,bio,location,parking,hours,emails,website&access_token=

// PAGE-ID/insights?metric=page_messages_new_conversations_unique,page_messages_blocked_conversations_unique&access_token=PAGE-ACCESS-TOKEN"