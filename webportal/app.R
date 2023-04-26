library(shiny)
library(shinydashboard)
library(DBI)
library(RJDBC)
library(data.table)
library(DT)

# Define the Athena JDBC driver and connection string
athena_driver <- JDBC('com.amazonaws.athena.jdbc.AthenaDriver', 'athena/AthenaJDBC41-2.0.9.jar')
connection_string <- 'jdbc:awsathena://athena.{region}.amazonaws.com:443'

# Connect to the Athena database
conn <- dbConnect(athena_driver, connection_string)

# Define the SQL query to retrieve data from the Athena database
sql_query <- 'SELECT * FROM fastq_results_table'

# Retrieve data from the Athena database and convert it to a data frame
results <- dbGetQuery(conn, sql_query)
results_df <- as.data.frame(results)

# Define the Shiny UI
ui <- dashboardPage(
    dashboardHeader(title = 'Athena Database Viewer'),
    dashboardSidebar(
        sidebarMenu(
            menuItem('Fastq Results', tabName = 'fastq_results', icon = icon('list-alt')),
            menuItem('Alignment Results', tabName = 'alignment_results', icon = icon('list-alt')),
            menuItem('Variant Results', tabName = 'variant_results', icon = icon('list-alt')),
            menuItem('Genome Assembly Results', tabName = 'genome_assembly_results', icon = icon('list-alt'))
        )
    ),
    dashboardBody(
        tabItems(
            tabItem(
                tabName = 'fastq_results',
                DT::dataTableOutput('fastq_results_table')
            ),
            tabItem(
                tabName = 'alignment_results',
                DT::dataTableOutput('alignment_results_table')
            ),
            tabItem(
                tabName = 'variant_results',
                DT::dataTableOutput('variant_results_table')
            ),
            tabItem(
                tabName = 'genome_assembly_results',
                DT::dataTableOutput('genome_assembly_results_table')
            )
        )
    )
)

# Define the Shiny server
server <- function(input, output) {
    # Define the output for the Fastq Results table
    output$fastq_results_table <- DT::renderDataTable(
        DT::datatable(
            results_df,
            filter = 'top',
            options = list(pageLength = 25)
        )
    )

    # Define the output for the Alignment Results table
    output$alignment_results_table <- DT::renderDataTable(
        DT::datatable(
            results_df,
            filter = 'top',
            options = list(pageLength = 25)
        )
    )

    # Define the output for the Variant Results table
    output$variant_results_table <- DT::renderDataTable(
        DT::datatable(
            results_df,
            filter = 'top',
            options = list(pageLength = 25)
        )
    )

    # Define the output for the Genome Assembly Results table
    output$genome_assembly_results_table <- DT::renderDataTable(
        DT::datatable(
            results_df,
            filter = 'top',
            options = list(pageLength = 25)
        )
    )
}

# Run the Shiny app
shinyApp(ui, server)

