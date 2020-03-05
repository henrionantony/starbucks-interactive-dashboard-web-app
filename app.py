import dash
import dash_bootstrap_components as dbc

external_scripts = [
    {
        'src': 'https://code.jquery.com/jquery-3.4.1.slim.min.js',
        'integrity': 'sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js',
        'integrity': 'sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js',
        'integrity': 'sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.js'
    }
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=external_scripts)
app.config.suppress_callback_exceptions = True

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        GOOGLE ANALYTICS SCRIPTS
        {%metas%}
        <title>Starbucks Interactive Dashboard</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <link href="https://fonts.googleapis.com/css?family=Nunito:400,600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.0/css/all.css" integrity="sha384-REHJTs1r2ErKBuJB0fCK99gCYsVjwxHrSU0N7I1zl9vZbggVJXRMsv/sLlOAGb4M" crossorigin="anonymous">
        {%favicon%}
        {%css%}
    </head>
    <body>
        
        <div class="top-nav">
        </div>
        <nav class="navbar">
            <button type="button" class="btn">View on Github<i class="fab fa-github-alt fa-lg"></i></button>
        </nav>
        {%app_entry%}
        <footer>
            <h2> Built with: </h2>
                <div class="logos">
                    <div class="slide"><img class="grayscale" src="/assets/images/python-logo.png" alt="python logo"></div>
                    <div class="slide"><img class="grayscale" src="/assets/images/dash-logo.png" alt="dash logo"></div>
                    <div class="slide"><img class="grayscale" src="/assets/images/plotly-logo.png" alt="plotly logo"></div>
                    <div class="slide"><img class="grayscale" src="/assets/images/html-logo.png" alt="html logo"></div>
                    <div class="slide"><img class="grayscale" src="/assets/images/css-logo.png" alt="css logo"></div>
                    <div class="slide"><img class="grayscale" src="/assets/images/bootstrap-logo.png" alt="bootstrap logo"></div>
                    <div class="slide"><img class="grayscale" src="/assets/images/mapbox-logo.png" alt="mapbox logo"></div>
                </div>
            {%config%}
            {%scripts%}
            {%renderer%} 
                <div class="footer">
                    <h3 class="footer-title">Antony Henrion</h3>
                    <div class="footer-icons">
                    <a aria-label="My Linkedin" target="_blank" href=""><i class="icon fab fa-linkedin-in"></i></a>
                    <a aria-label="My Github" target="_blank" href=""><i class="icon fab fa-github-alt" aria-hidden="true"></i></a>
                </div>
                </div>  
        </footer>
    </body>
</html>
'''
