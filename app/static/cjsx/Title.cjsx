Title = React.createClass
    getInitialState: ->
        title: "My Title"
    render: ->
        <div>
            <h2>Title: {this.state.title}</h2>
        </div>

Submitter = React.createClass
    render: ->
        <button type="button" class="btn btn-default">Submit</button>

SubmittedTitle = React.createClass
    render: ->
        <div>
            <Title />
            <Submitter />
        </div>

React.render React.createElement(SubmittedTitle, null), document.getElementById('content')