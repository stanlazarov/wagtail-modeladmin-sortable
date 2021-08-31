$(document).ready(function(){
    // Prevent sorting by fields as this breaks the ordering
    $("th a").each(function(){
        $(this).on('click', function(e){
            e.preventDefault()
        });
    });

    $( function() {
        var index_view_url = $('input[name="index_view_url').val()
        var csrf = $('input[name=csrfmiddlewaretoken]').val();

        sorter = $( "table.listing tbody" )

        sorter.sortable({
            helper: "clone",
            items: 'tr',
            axis: 'y',
            scroll: true,
            placeholder: "dropzone-placeholder",
            containment: 'main',
            appendTo: $('table.listing tbody'),
            start: function( event, ui ) {
                // Show elements on helper
                $("tr.ui-sortable-helper td ul.actions").css('display','table-cell');
                ui.helper.css('display','table')
                ui.helper.css('width','100%')
                field = ui.helper.children().first();
                field.css('display','table-cell');
                field.find('ul').css('visibility', 'hidden');
            },
            stop: function(event, ui) {
                var items = sorter.sortable("toArray", {attribute: 'data-object-pk'});

                if (items){
                    $.ajax({
                        url: index_view_url,
                        type: 'POST',
                        data: {
                            items: items,
                            csrfmiddlewaretoken: csrf,
                        },
                        success: function(response) {
                        },
                        error: function(response){
                        },
                    });
                }
            },
        });
        $( "table.listing tbody, tr, td, th" ).disableSelection();
      });
});
