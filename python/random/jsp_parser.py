input =  "" + "<!DOCTYPE html>" + "<html>" + "  <head class=<%=x%>>" + "    <% int i = 3 % 5, j = 2; %>" + "    <title>JSP Parser!</title>" + "  </head>" + "  <body>" + "    <h1>Time: <%= System.currentTimeMillis() %></h1>" + "    <p><code>i = <%=i%></code> and that's 33% more than <code>j = <%=j%></p>" + "  </body>" + "</html>"; 


#0 = print with quotes
#1 = print actual
#2 = print without quotes
state = 0
sys_line = "System.out.print("

def parse_input(input):
    output = []
    line = ""
    for index, char in enumerate(input):
        if char == '<':
            state = 0
            if input[index+1] == '%':
                output.append(sys_line + "\"" + line + "\")\n")
                line = ""
                state = 1
                if input[index+2] == '=':
                    state =2
            else:
                #state is html / 0
                line += char
        elif char == '>':
            if input[index -1] == "%":
                if state == 1:
                    output.append(line[1:-1] + "\n")
                    line = ""
                elif state == 2:
                    output.append(sys_line + line[2:-1] + ")\n")
                    line = ""
            else:
              line += char
        else:
            
            if len(line) == 0:
                if state == 1:
                    if char is not '%':
                        line += char
                elif state == 2:
                    if char is not '%' or char is not '=':
                        line += char
            else:
                line += char
                
        
    output.append(sys_line + "\"" + line + "\")\n")
    return "".join(output)
            

print parse_input(input)

"""
  /**
   * JSP Tags:
   *
   *  <% xyz %>
   *
   * where "xyz" is pure Java code
   *
   *  <%= xyz %>
   *
   * where "xyz" is passed to System.out.println.
   *
   * System.out.print("<!DOCTYPE html><html>  <head class=    ");
   * System.out.print(x);
   * System.out.print(">");
   * int i = 3 % 5, j = 2; ;
   * System.out.print("    <title>JSP Parser!</title>  </head>  <body>    <h1>Time: ");
   * System.out.print( System.currentTimeMillis() );
   * System.out.print("</h1>    <p><code>i = ");
   * System.out.print(i);
   * System.out.print("</code> and that's 33% more than <code>j = ");
   * System.out.print(j);
   * System.out.print("</p>  </body></html>");
   */
  public static String parse(String jsp) {
    // TODO Implement me!
    return "";
  }

  public static void main(String... args) {
    String jsp = ""
        + "<!DOCTYPE html>"
        + "<html>"
        + "  <head class=<%=x%>>"
        + "    <% int i = 3 % 5, j = 2; %>"
        + "    <title>JSP Parser!</title>"
        + "  </head>"
        + "  <body>"
        + "    <h1>Time: <%= System.currentTimeMillis() %></h1>"
        + "    <p><code>i = <%=i%></code> and that's 33% more than <code>j = <%=j%></p>"
        + "  </body>"
        + "</html>";
    //jsp += "<!-- <%=\"I'm in ur strings! <% <%= % > %> \"%> -->";

"""
