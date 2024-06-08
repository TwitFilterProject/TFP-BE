import { Injectable } from '@nestjs/common';
import FB from 'fb';

@Injectable()
export class AppService {
  accessToken: string;

  constructor() {
    this.accessToken = 'EAAb6aDIUTLcBO1rI4eb0P32ZAzB8CdMwums3NTPHKxZBMnhGNp7oDxzAd26zPsiekm6vlX8ZA2bRtIT0QZAz9Nd7xUSu86iGoOHW3UHM9ZAmPf123nrbHFsuZCggdChOIq2OK2aAZBLnRqmZC1GP8Y0F9l0HF1dtTuq9Ri3EL3ZCQE77JK17MSq8SEeOpnpX6eg0CWecZBxaLnX7lLqmEWXZCynKsGZC8xVg90rE'
    FB.setAccessToken(this.accessToken);
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

  getMsg(): Promise<any> {
    return new Promise((resolve, reject) => {
      FB.api(
        "/325237764009663",
        function (response: any) {
          if (response && !response.error) {
            resolve(response);
          }else {
            reject(response.error);
          }
        }
    );
    });
  }
}