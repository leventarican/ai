import chalk from "chalk";
import "dotenv/config";
import { ChatOpenAI } from "npm:@langchain/openai";
import { HumanMessage } from "npm:@langchain/core/messages";

console.log("# START    ");

// will use default env name OPENAI_API_KEY which is defined in .env
const model = new ChatOpenAI({
    modelName: "gpt-3.5-turbo-1106",
    temperature: 0.9,
});

const response = await model.invoke([
    new HumanMessage("write kotlin hello world.")
]);

console.log(chalk.bgGreenBright(response.content));

console.log("# END");