import { Controller, Get, Post, Query, Res } from '@nestjs/common';
import { AppService } from './app.service';


@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('getFeed')
  getFeed(): any {
    return this.appService.getFeed();
  }

  @Get('getImage')
  getImage(): any {
    return this.appService.getImage();
  }
}
