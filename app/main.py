from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from . import models
from .database import engine
from .routers import post, user, auth, vote

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/",response_class=HTMLResponse, include_in_schema= False )
def read_root():
    welcome_msg='''
                <html>
                <head>
                    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css'>
                    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css'>
                    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome-animation/0.2.1/font-awesome-animation.min.css'>
                    <style>
                        body
                        {
                        background: #000000;
                        }

                        .alert>.start-icon {
                            margin-right: 0;
                            min-width: 20px;
                            text-align: center;
                        }

                        .alert>.start-icon {
                            margin-right: 5px;
                        }

                        .greencross
                        {
                        font-size:18px;
                            color: #25ff0b;
                            text-shadow: none;
                        }

                        .alert-simple.alert-success
                        {
                        border: 1px solid rgba(36, 241, 6, 0.46);
                            background-color: rgba(7, 149, 66, 0.12156862745098039);
                            box-shadow: 0px 0px 2px #259c08;
                            color: #0ad406;
                        text-shadow: 2px 1px #00040a;
                        transition:0.5s;
                        cursor:pointer;
                        height: 500px;
                        }
                        .alert-success:hover{
                        background-color: rgba(7, 149, 66, 0.35);
                        transition:0.5s;
                        }
                        .alert-simple.alert-info
                        {
                        border: 1px solid rgba(6, 44, 241, 0.46);
                            background-color: rgba(7, 73, 149, 0.12156862745098039);
                            box-shadow: 0px 0px 2px #0396ff;
                            color: #0396ff;
                        text-shadow: 2px 1px #00040a;
                        transition:0.5s;
                        cursor:pointer;
                        }

                        .alert-info:hover
                        {
                        background-color: rgba(7, 73, 149, 0.35);
                        transition:0.5s;
                        }
                        .square_box {
                            position: absolute;
                            -webkit-transform: rotate(45deg);
                            -ms-transform: rotate(45deg);
                            transform: rotate(45deg);
                            border-top-left-radius: 45px;
                            opacity: 0.302;
                        }

                        .square_box.box_three {
                            background-image: -moz-linear-gradient(-90deg, #bdbdbd 0%, #d3d3d3 100%);
                            background-image: -webkit-linear-gradient(-90deg, #bdbdbd 0%, #d3d3d3 100%);
                            background-image: -ms-linear-gradient(-90deg, #bdbdbd 0%, #d3d3d3 100%);
                            opacity: 0.059;
                            left: -80px;
                            top: -60px;
                            width: 500px;
                            height: 500px;
                            border-radius: 45px;
                        }

                        .square_box.box_four {
                            background-image: -moz-linear-gradient(-90deg, #bdbdbd 0%, #d3d3d3 100%);
                            background-image: -webkit-linear-gradient(-90deg, #bdbdbd 0%, #d3d3d3 100%);
                            background-image: -ms-linear-gradient(-90deg, #bdbdbd 0%, #d3d3d3 100%);
                            opacity: 0.059;
                            left: 150px;
                            top: -25px;
                            width: 550px;
                            height: 550px;
                            border-radius: 45px;
                        }

                        .alert:before {
                            content: '';
                            position: absolute;
                            width: 0;
                            height: calc(100% - 44px);
                            border-left: 1px solid;
                            border-right: 2px solid;
                            border-bottom-right-radius: 3px;
                            border-top-right-radius: 3px;
                            left: 0;
                            top: 50%;
                            transform: translate(0,-50%);
                            height: 20px;
                        }

                        .fa-times
                        {
                        -webkit-animation: blink-1 2s infinite both;
                                    animation: blink-1 2s infinite both;
                        }


                        /**
                        * ----------------------------------------
                        * animation blink-1
                        * ----------------------------------------
                        */
                        @-webkit-keyframes blink-1 {
                        0%,
                        50%,
                        100% {
                            opacity: 1;
                        }
                        25%,
                        75% {
                            opacity: 0;
                        }
                        }
                        @keyframes blink-1 {
                        0%,
                        50%,
                        100% {
                            opacity: 1;
                        }
                        25%,
                        75% {
                            opacity: 0;
                        }
                        }
                    </style>
                </head>
                <body>
                    <section>
                    <div class="square_box box_three"></div>
                    <div class="square_box box_four"></div>
                    <div class="container mt-5">
                        <div class="row">
                        <div class="col-sm-12">
                            <div class="alert fade alert-simple alert-success alert-dismissible text-left font__family-montserrat font__size-16 font__weight-light brk-library-rendered rendered show">
                            <i class="start-icon far fa-grin-beam faa-tada animated"></i>
                            <strong class="font__weight-semibold">Hello People!</strong><br> &ensp;&ensp;&ensp; Welcome To My API Development Project
                            <p></p>
                            <p><strong class="font__weight-semibold">API-URLS:</strong></p>
                            Get all users api: <a style="text-decoration:none;" href="/users"> /users</a><br>
                            <a style="text-decoration:none;" href="/docs" target="blank"> all-api-urls <i class="fas fa-external-link-alt"></i></a>


                            </div>
                        </div>
                        </div>
                    </div>
                    </section>
                </body>
                </html>
                '''
    return welcome_msg

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)